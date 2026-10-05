#!/usr/bin/env python3
"""ARM valuation model - standard 10-yr scenario DCF, Oct 4 2026.

The AI-demand evidence check does NOT support a hypergrowth regime for Arm:
an IP licensor has no contracted chip backlog (RPO $2.07B, ~4.4 months of
guided revenue, declining and no longer reported), no lead-time/allocation
mechanism, and no take-or-pay volume commitments. Standard scenario DCF with
v2 inputs: revenue CAGRs 5.3/16.1/20.7%, FCF margins 25/32/33% (glided),
discounts 14.5/12/10.5% (12% base: beta ~3.8, Qualcomm litigation,
RISC-V, SoftBank/Arm-China related parties), terminal g 1.0/2.0/2.5%.
Outputs valuation_output.json consumed by build_note.py.
"""
import json

OUT = "/home/hatch/workspace/your_files/arm-equity-research/valuation_output.json"

PRICE = 307.49                      # Oct 2, 2026 close
SHARES = 1030.0                     # millions, diluted ADS
NET_CASH = 3900.0                   # $M, cash + ST investments June 30, 2026 (~$3.89B), negligible debt

F0 = 5600.0                         # $M, FY2027E revenue (Q1 act $1,289M + Q2 guide ~$1,380M + run-rate)

SCEN = {
    # bear: smartphone softness + RISC-V share loss + Qualcomm disruption; growth stalls
    "bear": dict(cagr=0.053, m0=0.252, m10=0.252, r=0.145, g=0.010,
                 desc="5.3% CAGR; FCF margin 25% flat; discount 14.5%; terminal g 1.0%."),
    # base: Neoverse/CSS royalty mix + AGI CPU ramp; strong but not bubble growth
    "base": dict(cagr=0.161, m0=0.255, m10=0.300, r=0.120, g=0.020,
                 desc="16.1% CAGR; FCF margin glides 27%->32%; discount 12.0%; terminal g 2.0%."),
    # bull: mgmt's $25B FYE31 plan haircut (CPU $15B->$8B); 20.7% CAGR
    "bull": dict(cagr=0.207, m0=0.265, m10=0.310, r=0.105, g=0.025,
                 desc="20.7% CAGR; FCF margin glides 28%->33%; discount 10.5%; terminal g 2.5%."),
}

def run(s):
    rev = F0
    pv = 0.0
    yrs = []
    for t in range(1, 11):
        rev *= 1 + s["cagr"]
        m = s["m0"] + (s["m10"] - s["m0"]) * t / 10
        fcf = rev * m
        pv += fcf / (1 + s["r"]) ** t
        yrs.append(dict(year=2026 + t, rev=rev, margin=m, fcf=fcf))
    fcf10 = yrs[-1]["fcf"]
    tv = fcf10 * (1 + s["g"]) / (s["r"] - s["g"])
    pv_tv = tv / (1 + s["r"]) ** 10
    ev = pv + pv_tv
    fv = (ev + NET_CASH) / SHARES
    return dict(fv=fv, ev=ev, pv_tv=pv_tv, tv_share=pv_tv / ev,
                rev10=yrs[-1]["rev"], fcf10=fcf10, yrs=yrs, desc=s["desc"])

res = {k: run(v) for k, v in SCEN.items()}
weighted = 0.25 * res["bear"]["fv"] + 0.50 * res["base"]["fv"] + 0.25 * res["bull"]["fv"]

payload = dict(
    meta=dict(ticker="ARM", name="Arm Holdings plc", price=PRICE, date="2026-10-04",
              shares_M=SHARES, net_cash_M=NET_CASH, rev2027E_M=F0,
              discounts=dict(bear=0.145, base=0.12, bull=0.105),
              terminal_g=dict(bear=0.01, base=0.02, bull=0.025),
              weights="25/50/25",
              qualification="NON-QUALIFIER: RPO $2.07B (~4.4 months of guided revenue, "
                           "declining, no longer reported); no lead-time/allocation mechanism in "
                           "IP licensing; no take-or-pay volume commitments; hyperscaler capex "
                           "commits to data centers/GPUs, not to Arm's IP category."),
    scenarios={k: {kk: vv for kk, vv in v.items() if kk != "yrs"} for k, v in res.items()},
    yearly={k: v["yrs"] for k, v in res.items()},
    weighted_fv=weighted,
    upside=(weighted - PRICE) / PRICE,
)
with open(OUT, "w") as f:
    json.dump(payload, f, indent=1)

for k in ("bear", "base", "bull"):
    r = res[k]
    print(f"{k:5s} FV ${r['fv']:6.2f}  rev10 ${r['rev10']/1e3:5.1f}B  fcf10 ${r['fcf10']/1e3:4.2f}B  TV/EV {r['tv_share']*100:4.1f}%")
print(f"WEIGHTED FV ${weighted:.2f}  upside {(weighted-PRICE)/PRICE*100:+.1f}% vs ${PRICE}")
print("wrote", OUT)
