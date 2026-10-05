"""WYNN 10-year FCFE scenario DCF — hardened methodology v2.
Base year 2026E. All $ millions unless noted. Judgment calls flagged [J]."""
import json

SHARES = 102.97          # diluted shares outstanding (yfinance 2026-10-02); old note used ~110M est [J: verified]
PRICE  = 75.88           # Oct 2, 2026 close

# ---- 2026E base ----
REV26, EBITDAR26 = 7500.0, 2270.0   # H1'26 EBITDAR $1,130.7M annualized; FY25 $2,224M

scen = {
 'base': dict(r=0.12,  g_term=0.020,
    core_g=[0.020,0.040,0.035,-0.030,0.030,0.025,0.025,0.020,0.020,0.020],
    margin=[0.298,0.303,0.308,0.295,0.305,0.310,0.310,0.310,0.310,0.310],
    term_margin=0.310,
    uae=[0,40,90,120,144,144,144,144,144,144],        # 40% of $360M proj EBITDA (25% haircut to $480M guide mid)
    enclave_rev=[0,0,160,320,320,320,320,320,320,320],# guide $400M rev, 20% haircut
    enclave_ebitda=[0,0,60,120,120,120,120,120,120,120],# guide $150-175M, 25% haircut
    interest=[600,595,590,580,570,560,550,545,540,535],
    tax=[130,135,140,145,150,155,160,165,170,175],
    maint=[400,408,416,424,433,442,450,459,468,478],
    uae_capex=[400,150,0,0,0,0,0,0,0,0],               # remaining ~$550M of ~$740M est. (rest spent H2'26)
    enclave_capex=[300,400,225,0,0,0,0,0,0,0],         # $925M total
    other_growth=[80]*10, nci=[110,113,117,120,124,127,131,135,139,143],
    corp=[150,153,156,159,162,166,169,172,176,179]),
 'bull': dict(r=0.105, g_term=0.025,
    core_g=[0.040,0.080,0.070,0.060,0.045,0.040,0.035,0.035,0.030,0.030],
    margin=[0.305,0.312,0.318,0.322,0.325,0.327,0.328,0.330,0.330,0.330],
    term_margin=0.320,                                 # normalized BELOW 33% peak
    uae=[0,60,130,170,200,200,200,200,200,200],        # 40% of $500M (guide high-end $570M, ~12% haircut)
    enclave_rev=[0,0,200,400,400,400,400,400,400,400],
    enclave_ebitda=[0,0,85,165,165,165,165,165,165,165],# guide midpoint, no haircut
    interest=[560,550,535,520,505,490,480,470,465,460],
    tax=[140,150,160,170,180,190,200,210,220,230],
    maint=[430,439,448,457,466,475,485,495,505,515],
    uae_capex=[350,100,0,0,0,0,0,0,0,0],
    enclave_capex=[325,400,200,0,0,0,0,0,0,0],
    other_growth=[90]*10, nci=[120,126,132,139,146,153,161,169,177,186],
    corp=[150,153,156,159,162,166,169,172,176,179]),
 'bear': dict(r=0.145, g_term=0.010,                       # terminal derated 50% vs base (>=25% required)
    core_g=[-0.040,-0.020,0.010,0.025,0.020,0.020,0.015,0.015,0.015,0.015],  # 10-yr CAGR <3%, early declines
    margin=[0.275,0.270,0.278,0.280,0.280,0.280,0.280,0.280,0.280,0.280],   # 300bp below base terminal margin
    term_margin=0.280,
    uae=[0,0,15,40,60,75,75,75,75,75],                 # delayed to mid-2028, 58% haircut to guide mid
    enclave_rev=[0,0,80,200,200,200,200,200,200,200],
    enclave_ebitda=[0,0,25,60,60,60,60,60,60,60],
    interest=[680,670,660,650,640,630,620,615,610,605],# refi wall at wider spreads
    tax=[90,85,90,95,100,105,110,115,120,125],
    maint=[350,357,364,371,379,386,394,402,410,418],   # deferred upkeep
    uae_capex=[450,400,50,0,0,0,0,0,0,0],              # +$300M equity call on overrun
    enclave_capex=[250,350,325,0,0,0,0,0,0,0],
    other_growth=[60]*10, nci=[80,78,82,86,90,94,98,102,106,110],
    corp=[150,153,156,159,162,166,169,172,176,179]),
}

out = {}
for name, s in scen.items():
    rev, fcfe, rows = REV26, [], []
    for t in range(10):
        rev = rev*(1+s['core_g'][t]) + s['enclave_rev'][t]
        ebitdar = rev*s['margin'][t] + s['uae'][t] + s['enclave_ebitda'][t]
        f = (ebitdar - s['corp'][t] - s['interest'][t] - s['tax'][t]
             - s['maint'][t] - s['uae_capex'][t] - s['enclave_capex'][t]
             - s['other_growth'][t] - s['nci'][t])
        fcfe.append(f); rows.append(dict(yr=2027+t, rev=round(rev), ebitdar=round(ebitdar), fcfe=round(f)))
    # terminal: year-10 FCFE recomputed at NORMALIZED mid-cycle margin (never peak)
    rev10 = rows[-1]['rev']
    ebitdar10n = rev10*s['term_margin'] + s['uae'][-1] + s['enclave_ebitda'][-1]
    f10n = (ebitdar10n - s['corp'][-1] - s['interest'][-1] - s['tax'][-1]
            - s['maint'][-1] - s['other_growth'][-1] - s['nci'][-1])
    tv = f10n*(1+s['g_term'])/(s['r']-s['g_term'])
    pv_fcfe = sum(f/(1+s['r'])**(t+1) for t, f in enumerate(fcfe))
    pv_tv = tv/(1+s['r'])**10
    eq = pv_fcfe + pv_tv
    out[name] = dict(fv_ps=round(eq/SHARES,2), pv_fcfe=round(pv_fcfe), pv_tv=round(pv_tv),
                     tv_share=round(pv_tv/eq,3), fcfes=[round(x) for x in fcfe],
                     rev10=rev10, tv_ps=round(pv_tv/SHARES,2), rows=rows,
                     r=s['r'], g_term=s['g_term'])

w = out['base']['fv_ps']*0.5 + out['bear']['fv_ps']*0.25 + out['bull']['fv_ps']*0.25
out['weighted'] = round(w,2)
out['upside'] = round((w-PRICE)/PRICE*100,1)
out['price'], out['shares'] = PRICE, SHARES
json.dump(out, open('/home/hatch/workspace/wynn-rebuild/valuation_output.json','w'), indent=1)
for k in ['bear','base','bull']:
    d = out[k]
    print(f"{k:5s} r={d['r']:.1%} g={d['g_term']:.1%}  FV/sh=${d['fv_ps']:.2f}  TV share of EQ={d['tv_share']:.0%}  FCFE10 path head={d['fcfes'][:3]}")
print(f"WEIGHTED FV = ${w:.2f}  vs ${PRICE}  upside {out['upside']:+.1f}%")
