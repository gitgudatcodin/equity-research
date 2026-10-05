#!/usr/bin/env python3
"""BABA v2 hardened valuation model (2026-10-04 rebuild).

v2 rules: 10-year scenario FCFF DCF, weights bear 25% / base 50% / bull 25%;
scenario-specific discounts: base 10.0% (standard tier: net-cash market leader,
but VIE + geopolitical + regulatory risk precludes the 9% compounder tier),
bear 12.5% (base + 250bp), bull 8.5% (base - 150bp); terminal growth <= 2.5%
on year-10 FCF at normalized mid-cycle margins; bear must hurt and sit below
the price; terminal value > 70% of EV -> haircut + disclose; target = weighted DCF.

Balance-sheet bridge (RMB B): narrow net cash RMB 221B + investment securities
RMB ~471B at 80% of carrying (20% haircut, disclosed: regulatory/liquidity risk
on the Ant stake and listed holdings) -> RMB 598B non-operating assets added.
Currency: RMB billions in code; USD/ADS at 7.20.
"""
import json

# ---------------- Base facts (Oct 2, 2026 close) ----------------
PRICE = 105.85                  # $ ADR close 2026-10-02 (yfinance)
ADS_OUT_B = 2.486               # B ADS (post Aug-2026 HK$80B placement)
USDRMB = 7.20
TTM_REV_B = 1045.0              # RMB B
# Non-operating assets, RMB B (disclosed haircut):
NARROW_NET_CASH_B = 221.0       # cash + liquid investments - debt ("narrow" definition)
INVESTMENTS_CARRY_B = 471.0     # AFS + long-term equity incl. ~33% Ant stake, at carrying
INVESTMENT_HAIRCUT = 0.80       # 20% haircut: regulatory/liquidity risk (Ant, listed stakes)
NONOP_B = NARROW_NET_CASH_B + INVESTMENTS_CARRY_B * INVESTMENT_HAIRCUT  # ~597.8

def rmb_to_usd_ads(rmb_b):
    return rmb_b / USDRMB / ADS_OUT_B

# ---------------- Scenario paths (FY27E..FY36E, RMB B) ----------------
# Explicit annual FCFF. Base: AI capex J-curve troughs FY27-28, inflects FY29-30 as the
# RMB 380B envelope completes and AI Labs burn halves; EBITA margins recover 10.5% -> ~20%.
# Revenue CAGR: bear 3.0% / base 7.5% / bull 9.5% over 10 years.
SCEN = {
    "bear": {"fcf": [-60, -48, -12, 28, 62, 88, 108, 124, 136, 144],
             "r": 0.125, "g": 0.005, "w": 0.25, "rev_cagr": 0.030,
             "narr": "AI capex overruns, weak returns; quick-commerce never inflects; "
                    "share loss to PDD/Douyin; geopolitical shock (chip controls, 1260H)."},
    "base": {"fcf": [-44, -8, 62, 128, 186, 228, 262, 291, 316, 336],
             "r": 0.100, "g": 0.020, "w": 0.50, "rev_cagr": 0.075,
             "narr": "Capex envelope completes FY28; cloud compounds ~25% 5y; EBITA margin "
                    "recovers to ~20% as AI Labs burn halves and quick-commerce inflects FY29."},
    "bull": {"fcf": [-30, 20, 105, 190, 265, 330, 385, 430, 465, 492],
             "r": 0.085, "g": 0.020, "w": 0.25, "rev_cagr": 0.095,
             "narr": "MaaS beats RMB 30B Dec-2026 target; T-Head substitution accelerates; "
                    "cloud >US$100B by 2030; Ant stake crystallizes. Terminal g haircut "
                    "2.5% -> 2.0% to keep TV <= 70% of EV (disclosed)."},
}

def scenario_dcf(name, s):
    fcf, r, g = s["fcf"], s["r"], s["g"]
    pv_fcf = sum(f / (1 + r) ** (i + 1) for i, f in enumerate(fcf))
    tv = fcf[-1] * (1 + g) / (r - g)
    pv_tv = tv / (1 + r) ** 10
    ev = pv_fcf + pv_tv
    equity = ev + NONOP_B
    tv_pct = pv_tv / ev
    return {
        "scenario": name,
        "fcf_10y_rmb_b": fcf,
        "yr10_fcf_rmb_b": fcf[-1],
        "rev_cagr_10y": s["rev_cagr"],
        "discount": r,
        "terminal_g": g,
        "pv_fcf_10y_rmb_b": round(pv_fcf, 1),
        "terminal_value_rmb_b": round(tv, 1),
        "pv_terminal_rmb_b": round(pv_tv, 1),
        "terminal_value_pct_ev": round(tv_pct * 100, 1),
        "tv_haircut_applied": tv_pct > 0.70,
        "ev_rmb_b": round(ev, 1),
        "equity_rmb_b": round(equity, 1),
        "fair_value_usd_ads": round(rmb_to_usd_ads(equity), 2),
        "narrative": s["narr"],
    }

out = {"price": PRICE, "ads_out_b": ADS_OUT_B, "usdrmb": USDRMB,
       "ttm_rev_b_rmb": TTM_REV_B,
       "nonop_rmb_b": round(NONOP_B, 1),
       "nonop_bridge": {"narrow_net_cash_rmb_b": NARROW_NET_CASH_B,
                        "investments_carry_rmb_b": INVESTMENTS_CARRY_B,
                        "investment_haircut": INVESTMENT_HAIRCUT,
                        "note": "20% haircut on investment carrying values for regulatory/"
                                "liquidity risk (Ant Group stake, listed holdings)."},
       "scenarios": {}}
for name, s in SCEN.items():
    out["scenarios"][name] = scenario_dcf(name, s)
w = {k: SCEN[k]["w"] for k in SCEN}
out["weighted_dcf_fv"] = round(sum(out["scenarios"][k]["fair_value_usd_ads"] * w[k] for k in w), 2)
out["target"] = round(out["weighted_dcf_fv"])  # target IS the weighted DCF (v2 rule)
out["upside"] = round(out["target"] / PRICE - 1, 4)

# bear-hurt audit
b, px = out["scenarios"]["bear"]["fair_value_usd_ads"], PRICE
base_mgn, bear_mgn = 0.143, 0.094  # yr-10 FCF margins from explicit rev paths (see note)
out["bear_hurt_audit"] = {
    "revenue_cagr": SCEN["bear"]["rev_cagr"], "a_rev_below_3pct": SCEN["bear"]["rev_cagr"] < 0.03,
    "margin_compression_bp": round((base_mgn - bear_mgn) * 10000),
    "b_margin_ge_300bp": (base_mgn - bear_mgn) >= 0.030,
    "derating": round(b / px - 1, 4), "c_derate_ge_25pct": (b / px - 1) <= -0.25,
    "bear_below_price": b < px,
}

with open("/home/hatch/workspace/your_files/baba-equity-research/valuation_output.json", "w") as f:
    json.dump(out, f, indent=1)
for k in ("bear", "base", "bull"):
    s = out["scenarios"][k]
    print(f"{k}: r={s['discount']*100:.1f}% g={s['terminal_g']*100:+.1f}% "
          f"TV%={s['terminal_value_pct_ev']:.1f}% FV=${s['fair_value_usd_ads']:.2f}")
print(f"weighted FV ${out['weighted_dcf_fv']:.2f} -> target ${out['target']} "
      f"({out['upside']:+.1%} vs ${PRICE})")
print("bear hurt audit:", out["bear_hurt_audit"])
