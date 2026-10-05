#!/usr/bin/env python3
"""Addendum C hypergrowth-regime DCFs for AMD and NVDA.
10-yr scenario DCF, weights bear 25% / base 50% / bull 25%.
v2 discount structure: bear = base + 250bp, bull = base - 150bp (floor 8%).
Terminal growth <= 2.5% on year-10 FCF at normalized through-cycle (not peak) margins.
Research analysis, not investment advice. As of Oct 4, 2026 (Oct 2 closes).
"""
import json

def dcf(rev, fcfm, r, tg, net_cash, shares, label):
    """rev/fcfm: lists covering yr0..yr10 (yr0 = anchor year). Returns per-share FV."""
    fcff = [rev[i] * fcfm[i] for i in range(len(rev))]
    pv = sum(fcff[i] / (1 + r) ** i for i in range(1, len(rev)))
    tv = fcff[-1] * (1 + tg) / (r - tg)
    pv_tv = tv / (1 + r) ** (len(rev) - 1)
    ev = pv + pv_tv
    eq = ev + net_cash
    fv = eq / shares
    return {
        "label": label, "discount": r, "terminal_g": tg,
        "revenues": [round(x, 1) for x in rev],
        "fcf_margins": [round(x, 3) for x in fcfm],
        "fcff": [round(x, 2) for x in fcff],
        "pv_explicit": round(pv, 2), "terminal_value": round(tv, 2),
        "pv_terminal": round(pv_tv, 2), "tv_share_of_ev": round(pv_tv / ev, 3),
        "enterprise_value": round(ev, 2), "equity_value": round(eq, 2),
        "shares_bn": shares, "fair_value_per_share": round(fv, 2),
    }

def weighted(scenarios):
    w = {"bear": 0.25, "base": 0.50, "bull": 0.25}
    return round(sum(scenarios[k]["fair_value_per_share"] * w[k] for k in w), 2)

# ================= AMD =================
# Anchor: FY2026E $48.5B (Q1 $8.6 + Q2 $11.54 + Q3 guide $13.0 + Q4 ~$15.4 Helios ramp)
# Mgmt guide (Citi TMT Sep 2026): 2027 DC ~$70B, AI GPUs low-$40B; customer forecasts
# (Meta/OpenAI/Anthropic) above partnership levels. 14GW committed across 3 customers.
amd_rev = {
    "bear": [48.5, 72.0, 70.0, 61.0, 59.0, 62.0, 67.0, 73.0, 79.0, 85.0, 91.0],
    "base": [48.5, 90.0, 118.0, 140.0, 157.0, 171.0, 184.0, 196.0, 205.0, 213.0, 220.0],
    "bull": [48.5, 99.0, 139.0, 174.0, 207.0, 240.0, 271.0, 300.0, 324.0, 344.0, 362.0],
}
amd_fcfm = {
    "bear": [0.08, 0.09, 0.07, 0.05, 0.05, 0.06, 0.07, 0.08, 0.10, 0.12, 0.13],
    "base": [0.10, 0.12, 0.13, 0.14, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18],
    "bull": [0.11, 0.13, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.215, 0.22],
}
AMD_PRICE, AMD_NETCASH = 633.91, 8.8  # Oct 2 close; net cash $13.1B - $4.3B debt
amd = {
    "bear": dcf(amd_rev["bear"], amd_fcfm["bear"], 0.145, 0.00, AMD_NETCASH, 1.70, "bear"),
    "base": dcf(amd_rev["base"], amd_fcfm["base"], 0.120, 0.02, AMD_NETCASH, 1.80, "base"),
    "bull": dcf(amd_rev["bull"], amd_fcfm["bull"], 0.105, 0.02, AMD_NETCASH, 1.95, "bull"),
}
amd_w = weighted(amd)

# ================= NVDA =================
# Anchor: FY2027E $396B (Q2 FY27 $96.22B, Q3 guide $108B; FY26 $215.94B).
# Mgmt guide (Aug 2026): FY28 (ends Jan 2028) revenue +~70% YoY (~$670B), supply-constrained;
# "real demand is much higher." Rubin in full production since Mar 2026.
nvda_rev = {
    "bear": [396, 545, 450, 418, 446, 482, 517, 552, 586, 620, 655],
    "base": [396, 673, 850, 1000, 1120, 1220, 1300, 1365, 1420, 1470, 1522],
    "bull": [396, 745, 970, 1200, 1400, 1600, 1750, 1860, 1950, 2030, 2100],
}
nvda_fcfm = {
    "bear": [0.33, 0.28, 0.24, 0.26, 0.30, 0.33, 0.35, 0.36, 0.38, 0.39, 0.39],
    "base": [0.35, 0.36, 0.38, 0.40, 0.42, 0.44, 0.45, 0.46, 0.47, 0.475, 0.48],
    "bull": [0.36, 0.38, 0.40, 0.42, 0.44, 0.46, 0.47, 0.48, 0.49, 0.50, 0.50],
}
NVDA_PRICE, NVDA_NETCASH = 233.95, 18.2  # Oct 2 close; $22.4B cash + $34.1B mktbl debt sec - $38.4B debt
nvda = {
    "bear": dcf(nvda_rev["bear"], nvda_fcfm["bear"], 0.145, 0.015, NVDA_NETCASH, 24.3, "bear"),
    "base": dcf(nvda_rev["base"], nvda_fcfm["base"], 0.120, 0.025, NVDA_NETCASH, 23.5, "base"),
    "bull": dcf(nvda_rev["bull"], nvda_fcfm["bull"], 0.105, 0.025, NVDA_NETCASH, 22.8, "bull"),
}
nvda_w = weighted(nvda)

out = {
    "as_of": "2026-10-04 (Oct 2, 2026 closes)", "weights": {"bear": 0.25, "base": 0.50, "bull": 0.25},
    "AMD": {"price": AMD_PRICE, "scenarios": amd, "weighted_fv": amd_w,
            "upside": round(amd_w / AMD_PRICE - 1, 4)},
    "NVDA": {"price": NVDA_PRICE, "scenarios": nvda, "weighted_fv": nvda_w,
             "upside": round(nvda_w / NVDA_PRICE - 1, 4)},
}
print(json.dumps(out, indent=1))
for t in ("AMD", "NVDA"):
    print(f"\n=== {t} ===")
    for k in ("bear", "base", "bull"):
        s = out[t]["scenarios"][k]
        cagr = (s["revenues"][-1] / s["revenues"][0]) ** (1 / 10) - 1
        print(f"{k:5s} FV ${s['fair_value_per_share']:>8}  revCAGR {cagr:6.1%}  "
              f"yr10 fcfm {s['fcf_margins'][-1]:5.1%}  TV/EV {s['tv_share_of_ev']:.0%}  "
              f"rev10 ${s['revenues'][-1]:,.0f}B")
    print(f"weighted FV ${out[t]['weighted_fv']}  vs ${out[t]['price']}  "
          f"upside {out[t]['upside']:+.1%}")

with open("/home/hatch/workspace/your_files/amd-equity-research/model_addendum_c.json", "w") as f:
    json.dump({"AMD": out["AMD"], **{"weights": out["weights"], "as_of": out["as_of"]}}, f, indent=1)
with open("/home/hatch/workspace/your_files/nvda-equity-research/model_addendum_c.json", "w") as f:
    json.dump({"NVDA": out["NVDA"], **{"weights": out["weights"], "as_of": out["as_of"]}}, f, indent=1)
print("\nmodel JSONs written")
