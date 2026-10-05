#!/usr/bin/env python3
"""Coinbase (COIN) valuation: cycle-aware scenario DCF, mid-cycle FCF power,
SOTP, reverse-DCF. $ millions unless noted.

Anchors (verified 2026-09-30):
  price $186.41 | 52wk $139.11-$402.16 | ATH ~$420 (Jul-2025)
  diluted shares ~285M (Q3'25: 292M incl. 29M dilutive + 11M Deribit shares;
    Q2'26 basic 263.4M in a loss quarter)
  cash/cash-eq + restricted $13,150M | LT debt $5,900M -> net cash ~$7,000M
    (conservative haircut for restricted/customer cash)
  EV ~$46.1B | TTM revenue $6,044M | beta ~3.34
  2025: total rev $7,181M (txn $4,055M: consumer $3,323/inst. $480/other $253;
    S&S $2,828M: stablecoin $1,349/blockchain rewards $677/interest&finance $247/other $555)
  H1'26: total rev $2,633M (Q1 $1,413 / Q2 $1,220); adj. EBITDA Q2 $207.8M (-59% YoY)
  Q3'26 guide: S&S $500-580M; FY26E adj. expenses $4.2-4.45B (narrowed)
  BTC $83.4k vs $123.5k Oct-2025 peak; COIN -54% from $402 peak
  Take rate (retail blended): 1.91% (2023) -> 1.55% (2024) -> 1.39% (2025) -> ~1.35% (2026E)
  SBC ~$240M/qtr (~$1B/yr); 14 straight quarters of positive adj. EBITDA
"""
import json

OUT = "/home/hatch/workspace/coin-research/valuation_output.json"

PRICE = 186.41
SHARES = 285.0
NET_CASH = 7000.0
EV = PRICE * SHARES - NET_CASH

# Crypto ~4-yr cycles: peak Oct-2025, trough 2026, recovery 2027-28,
# next peak ~2029 (post Apr-2028 halving), post-peak normalization 2030.
# Total revenue paths, $B, 2026..2035.
SCEN = {
    "bear": {  # winter extends; take-rate compression accelerates; rates cut USDC income
        "rev":  [5.0, 4.8, 5.4, 6.2, 7.2, 6.4, 7.0, 7.6, 8.2, 8.8],
        "fcfm": [0.08, 0.06, 0.12, 0.18, 0.22, 0.16, 0.20, 0.22, 0.23, 0.24],
        "wacc": 0.115, "g": 0.02, "w": 0.25,
    },
    "base": {  # cycle repeats; S&S compounds ~12%/yr; take rates stabilize
        "rev":  [5.1, 6.6, 7.9, 8.8, 9.6, 8.0, 9.0, 10.0, 11.0, 12.0],
        "fcfm": [0.14, 0.20, 0.27, 0.33, 0.37, 0.27, 0.29, 0.31, 0.32, 0.33],
        "wacc": 0.11, "g": 0.03, "w": 0.50,
    },
    "bull": {  # everything-exchange works; GENIUS + tokenized stocks + prediction mkts scale
        "rev":  [5.3, 7.5, 10.0, 11.5, 13.0, 11.5, 13.5, 15.5, 17.5, 19.5],
        "fcfm": [0.16, 0.24, 0.32, 0.38, 0.42, 0.34, 0.36, 0.37, 0.38, 0.39],
        "wacc": 0.105, "g": 0.035, "w": 0.25,
    },
}

def dcf_value(rev, fcfm, wacc, g):
    fcf = [r * 1000 * m for r, m in zip(rev, fcfm)]
    pv = sum(f / (1 + wacc) ** (i + 1) for i, f in enumerate(fcf))
    tv = fcf[-1] * (1 + g) / (wacc - g) / (1 + wacc) ** 10
    ev = pv + tv
    return {"pv_fcf": round(pv, 1), "tv": round(tv, 1), "ev": round(ev, 1),
            "eq": round(ev + NET_CASH, 1),
            "per_share": round((ev + NET_CASH) / SHARES, 2)}

scen_out = {n: dcf_value(s["rev"], s["fcfm"], s["wacc"], s["g"]) for n, s in SCEN.items()}
for n in scen_out: scen_out[n]["weight"] = SCEN[n]["w"]
blended = sum(scen_out[n]["per_share"] * SCEN[n]["w"] for n in SCEN)

# ---- Mid-cycle FCF power: normalized rev $7.2B x 30% FCF margin = $2.16B
MID_FCF = 7.2 * 1000 * 0.30
midcycle = {f"{m}x": round((MID_FCF * m + NET_CASH) / SHARES, 2) for m in (16, 18, 20, 22)}

# ---- SOTP: S&S run-rate ~$2.5B (sticky, 9-10x rev); txn run-rate ~$2.6B (cyclical, 3.5-4.5x)
sotp = {}
for sm, tm in [(8, 3.5), (9, 4.0), (10, 4.5)]:
    sotp[f"S&S {sm}x / txn {tm}x"] = round((2500 * sm + 2600 * tm + NET_CASH) / SHARES, 2)

# ---- Reverse DCF: normalized FCF $2.16B, 5 yrs at 10%, WACC 11% -> implied perp g at $186.41
def implied_g():
    target_ev = PRICE * SHARES - NET_CASH
    f0, g1, wacc = MID_FCF, 0.10, 0.11
    pv1 = sum(f0 * (1 + g1) ** i / wacc**0 / (1 + wacc) ** i for i in range(1, 6))
    f5 = f0 * (1 + g1) ** 5
    lo, hi = 0.0, 0.109
    for _ in range(80):
        g = (lo + hi) / 2
        val = pv1 + f5 * (1 + g) / (wacc - g) / (1 + wacc) ** 5
        if val < target_ev: lo = g
        else: hi = g
    return round((lo + hi) / 2, 4)

result = {
    "inputs": {"price": PRICE, "diluted_shares_M": SHARES, "net_cash_M": NET_CASH,
               "ev_M": round(EV), "ttm_revenue_M": 6044, "fye2026E_revenue_B": 5.1},
    "scenario_dcf": scen_out,
    "blended_dcf_fair_value": round(blended, 2),
    "midcycle_fcf_power": {"normalized_fcf_M": MID_FCF, "per_share": midcycle},
    "sotp_per_share": sotp,
    "reverse_dcf_implied_perpetual_growth": implied_g(),
}
json.dump(result, open(OUT, "w"), indent=1)
print(json.dumps(result, indent=1))
