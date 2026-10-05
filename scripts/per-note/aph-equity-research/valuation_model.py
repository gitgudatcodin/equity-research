#!/usr/bin/env python3
"""APH valuation model - segment-level 10-yr scenario DCF, Oct 4 2026.

AI-datacom slice (43% of sales, hypergrowth regime: years 1-3 at/near guidance,
duration/fade assumptions per scenario) vs non-AI rest (standard assumptions).
10-yr explicit FCFF, weights 25/50/25. Discounts keep v2 structure: 11.5/9/8.
Terminal g 1.5/2.5/2.5 on through-cycle (not peak) margins.
Outputs valuation_output.json consumed by build_note.py.
"""
import json

OUT = "/home/hatch/workspace/your_files/aph-equity-research/valuation_output.json"

PRICE = 86.96                      # Oct 2, 2026 close
SHARES = 2578.4                    # millions, diluted, post 2:1 split (Sep 3, 2026)
NET_DEBT = 13400.0                 # $M, June 30, 2026 (CFO: total debt $18.8B, net debt $13.4B)

# ---- FY2026E revenue base ($M): Q1 act 7,600 / Q2 act 8,760 / Q3 guide mid 9,350 / Q4 est 9,650
REV26 = 7600.0 + 8760.0 + 9350.0 + 9650.0      # 35,360
AI_SHARE = 0.43                                 # IT datacom = 43% of Q2 2026 sales, co's largest end market
AI0 = REV26 * AI_SHARE
REST0 = REV26 * (1 - AI_SHARE)

# ---- Scenarios: AI-slice growth path (years 2027-2036), rest growth, through-cycle FCF margins
SCEN = {
    "bear": dict(
        ai=[0.25, -0.20, -0.10, -0.02, 0.03, 0.04, 0.05, 0.05, 0.05, 0.05],
        rest=[0.01] * 10, m_ai=0.15, m_rest=0.09, r=0.115, g=0.015,
        dur="Supercycle ends 2027. 2028 cliff: AI-slice revenue -20% as book-to-bill "
            "collapses below 1.0, LTA orders renegotiated, channel inventory glut; "
            "-10% in 2029; slow recovery from 2031. AI margin compresses to 15% (peak-mix reverses)."),
    "base": dict(
        ai=[0.50, 0.35, 0.28, 0.18, 0.12, 0.09, 0.07, 0.06, 0.05, 0.05],
        rest=[0.045] * 10, m_ai=0.18, m_rest=0.115, r=0.09, g=0.025,
        dur="Supercycle runs through 2030 (hyperscaler AI-capex wave as committed), then "
            "fades: +12% in 2031 stepping to +5% by 2035-36 as penetration saturates. "
            "AI margins through-cycle 18% (below the 2026 record mix, above the old base)."),
    "bull": dict(
        ai=[0.60, 0.50, 0.45, 0.35, 0.28, 0.22, 0.15, 0.12, 0.09, 0.07],
        rest=[0.065] * 10, m_ai=0.19, m_rest=0.13, r=0.08, g=0.025,
        dur="Supercycle runs through 2033: agentic/inference disaggregation raises networking "
            "intensity per unit of compute, keeping interconnect demand ahead of capacity; "
            "fade 2034-36 toward high-single digits. AI margins 19% through-cycle."),
}

def run(s):
    ai, rest = AI0, REST0
    pv = 0.0
    yrs = []
    for t, (ga, gr) in enumerate(zip(s["ai"], s["rest"]), start=1):
        ai *= 1 + ga
        rest *= 1 + gr
        fcf = ai * s["m_ai"] + rest * s["m_rest"]
        pv += fcf / (1 + s["r"]) ** t
        yrs.append(dict(year=2026 + t, ai=ai, rest=rest, rev=ai + rest, fcf=fcf))
    fcf10 = yrs[-1]["fcf"]
    tv = fcf10 * (1 + s["g"]) / (s["r"] - s["g"])
    pv_tv = tv / (1 + s["r"]) ** 10
    ev = pv + pv_tv
    fv = (ev - NET_DEBT) / SHARES
    rev10 = yrs[-1]["rev"]
    cagr = (rev10 / REV26) ** (1 / 10) - 1
    return dict(fv=fv, ev=ev, pv_explicit=pv, pv_tv=pv_tv, tv_share=pv_tv / ev,
                rev10=rev10, cagr=cagr, fcf10=fcf10, yrs=yrs, dur=s["dur"])

res = {k: run(v) for k, v in SCEN.items()}
weighted = 0.25 * res["bear"]["fv"] + 0.50 * res["base"]["fv"] + 0.25 * res["bull"]["fv"]

payload = dict(
    meta=dict(ticker="APH", name="Amphenol Corporation", price=PRICE, date="2026-10-04",
              shares_M=SHARES, net_debt_M=NET_DEBT, rev2026E_M=REV26, ai_share=AI_SHARE,
              ai0_M=AI0, rest0_M=REST0,
              discounts=dict(bear=0.115, base=0.09, bull=0.08),
              terminal_g=dict(bear=0.015, base=0.025, bull=0.025),
              weights="25/50/25"),
    scenarios={k: {kk: vv for kk, vv in v.items() if kk != "yrs"} for k, v in res.items()},
    yearly={k: v["yrs"] for k, v in res.items()},
    weighted_fv=weighted,
    upside=(weighted - PRICE) / PRICE,
)
with open(OUT, "w") as f:
    json.dump(payload, f, indent=1)

for k in ("bear", "base", "bull"):
    r = res[k]
    print(f"{k:5s} FV ${r['fv']:7.2f}  rev10 ${r['rev10']/1e3:6.1f}B  CAGR {r['cagr']*100:5.2f}%  "
          f"fcf10 ${r['fcf10']/1e3:5.2f}B  TV/EV {r['tv_share']*100:4.1f}%")
print(f"WEIGHTED FV ${weighted:.2f}  upside {(weighted-PRICE)/PRICE*100:+.1f}% vs ${PRICE}")
print("wrote", OUT)
