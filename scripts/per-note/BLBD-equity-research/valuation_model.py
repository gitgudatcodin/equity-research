#!/usr/bin/env python3
"""Blue Bird Corporation (NASDAQ: BLBD) valuation — six pricing models. All figures USD.

Anchors (Oct 3, 2026 dossier):
- Price $56.53 (10/2/26 close); 52-wk $46.14-$83.39; ~33.5M diluted shares (est., incl. Micro Bird stock consideration)
- Net CASH ~$25M ($117M cash - $91M term loan at 6/27/26) -> EV ~= $1.87B
- FY2026E guidance (raised 8/5/26): revenue $1.74-1.76B, adj. EBITDA $245-250M, adj. FCF $125-135M
- FY2026E adj. EPS ~$4.55 (9-mo adj. EPS $3.29 + Q4); Q3 GAAP EPS $5.27 distorted by $160.5M one-time
  Micro Bird remeasurement gain — model uses ADJUSTED figures throughout
- Consensus: Buy, avg target $85.33 (9 analysts)
"""
import json

PRICE = 56.53
SHARES = 33.5e6            # diluted, est. incl. ~2.2M Micro Bird stock consideration
NET_CASH = 25e6            # net debt is negative
WACC = 0.10

REV_2026E = 1750e6
EBITDA_2026E = 247e6       # 14.1% margin
FCF_2026E = 130e6
EPS_2026E_ADJ = 4.55
EPS_2027E_ADJ = 5.10       # est., +12%

def fcf_path(rev_cagr, margin_path, years=5):
    """Explicit FCF 2027-2031. margin_path: list of EBITDA margins."""
    revs, eb, fc = [], [], []
    for i, m in enumerate(margin_path, 1):
        r = REV_2026E * (1 + rev_cagr) ** i
        e = r * m
        dna = 22e6
        ebit = e - dna
        capex = 42e6                       # maintenance + EV plant growth capex
        interest = 6e6
        tax = max(0.0, 0.24 * (ebit - interest))
        wc = 0.01 * (r - (REV_2026E * (1 + rev_cagr) ** (i - 1)))  # 1% of incremental revenue
        f = e - capex - interest - tax - wc
        revs.append(r); eb.append(e); fc.append(f)
    return revs, eb, fc

def pv_ev(fcf_list, g_term):
    pv_e = sum(f / (1 + WACC) ** i for i, f in enumerate(fcf_list, 1))
    tv = fcf_list[-1] * (1 + g_term) / (WACC - g_term)
    return pv_e + tv / (1 + WACC) ** len(fcf_list)

def scenario_ps(rev_cagr, margins, g_term, label):
    revs, eb, fc = fcf_path(rev_cagr, margins)
    ev = pv_ev(fc, g_term)
    eq = ev + NET_CASH
    return {"label": label, "rev_cagr": rev_cagr, "g_term": g_term,
            "rev_2031_bn": round(revs[-1] / 1e9, 2),
            "ebitda_2031_m": round(eb[-1] / 1e6, 0),
            "fcf_2031_m": round(fc[-1] / 1e6, 0),
            "fcf_path_m": [round(x / 1e6, 0) for x in fc],
            "ev_bn": round(ev / 1e9, 2), "eq_bn": round(eq / 1e9, 2),
            "per_share": round(eq / SHARES, 2)}

# Bear: EPA revamp stalls EV, tariff drag, school budgets tighten; margin 13.5%
bear = scenario_ps(0.03, [0.138, 0.136, 0.135, 0.135, 0.135], 0.015, "bear")
# Base: replacement cycle + EV ramp + Micro Bird + parts; Ford chassis contributes from 2028; margin -> 15%
base = scenario_ps(0.07, [0.143, 0.145, 0.147, 0.148, 0.150], 0.025, "base")
# Bull: EPA NOFO favorable, Ford chassis ramps, EV leadership compounds; margin -> 15.5%+
bull = scenario_ps(0.11, [0.146, 0.149, 0.152, 0.154, 0.156], 0.030, "bull")

weighted = 0.25 * bear["per_share"] + 0.50 * base["per_share"] + 0.25 * bull["per_share"]

# --- Model 2: EV/EBITDA relative multiples (industrial OEM peers 8-10x; BLBD ~7.6x today)
ev_ebitda = {m: {"ev_bn": round((m * EBITDA_2026E) / 1e9, 2),
                 "per_share": round((m * EBITDA_2026E + NET_CASH) / SHARES, 2)}
             for m in (8.0, 9.0, 10.0)}

# --- Model 3: P/E on FY2027E adjusted EPS $5.10
pe = {m: round(m * EPS_2027E_ADJ, 2) for m in (13, 15, 17)}

# --- Model 4: Reverse DCF — what perpetual FCF growth is $56.53 pricing?
EV_MKT = PRICE * SHARES - NET_CASH
FCF_NORM = 150e6   # normalized FCF (FY27E-ish run-rate)
# EV = FCF*(1+g)/(WACC-g) -> solve g
g_impl = (EV_MKT * WACC - FCF_NORM) / (EV_MKT + FCF_NORM)

# --- Model 5: Sum-of-the-parts
core_ev = 8.5 * 240e6                                  # core school-bus EBITDA ~$240M ex-Ford
ford_ebitda_2032 = 80e6                                # Ford F53/59 steady-state EBITDA (mgmt case)
ford_pv = 0.60 * (8.0 * ford_ebitda_2032) / (1 + WACC) ** 6   # 60% probability-weighted
sotp_eq = core_ev + ford_pv + NET_CASH
sotp = {"core_ev_bn": round(core_ev / 1e9, 2),
        "ford_option_pv_m": round(ford_pv / 1e6, 0),
        "net_cash_m": round(NET_CASH / 1e6, 0),
        "per_share": round(sotp_eq / SHARES, 2)}

# --- Model 6: FCF-yield fair value (normalized FCF at fair yield)
fcf_yield = {y: round((FCF_NORM / y + NET_CASH) / SHARES, 2) for y in (0.055, 0.065, 0.075)}

out = {
    "as_of": "2026-10-03", "price": PRICE, "shares_m": round(SHARES / 1e6, 1),
    "market_cap_bn": round(PRICE * SHARES / 1e9, 2),
    "net_cash_m": round(NET_CASH / 1e6, 0),
    "ev_bn": round(EV_MKT / 1e9, 2),
    "fy2026e": {"revenue_bn": round(REV_2026E / 1e9, 2), "adj_ebitda_m": round(EBITDA_2026E / 1e6, 0),
                "adj_fcf_m": round(FCF_2026E / 1e6, 0), "adj_eps": EPS_2026E_ADJ},
    "dcf_bear": bear, "dcf_base": base, "dcf_bull": bull,
    "dcf_weighted": round(weighted, 2),
    "ev_ebitda": ev_ebitda, "ebitda_2026e_m": round(EBITDA_2026E / 1e6, 0),
    "pe_model": pe, "eps_2027e_adj": EPS_2027E_ADJ,
    "reverse_dcf": {"ev_mkt_bn": round(EV_MKT / 1e9, 2),
                    "normalized_fcf_m": round(FCF_NORM / 1e6, 0),
                    "implied_perpetual_fcf_growth": round(g_impl * 100, 1)},
    "sotp": sotp,
    "fcf_yield_model": fcf_yield, "fcf_norm_m": round(FCF_NORM / 1e6, 0),
    "consensus_target": 85.33, "consensus_range": [62.0, 95.0],
}
out["target"] = 78.0
out["upside_vs_price"] = round((78.0 - PRICE) / PRICE * 100, 1)
with open("/home/hatch/workspace/blbd-research/valuation_output.json", "w") as f:
    json.dump(out, f, indent=2)
print(json.dumps(out, indent=2))
