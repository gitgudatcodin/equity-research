#!/usr/bin/env python3
"""McDonald's (MCD) valuation models — DCF, forward P/E, EV/EBITDA, Gordon DDM."""
import math

# ---------- Inputs (grounded in research dossier, Sep 2026) ----------
PRICE = 236.50
SHARES_M = 710.0            # diluted shares (~167.5B / 236.50)
NET_DEBT_B = 39.2          # LT debt 39.97B - cash 0.77B (12/31/25)
DIV0 = 7.72                # annualized dividend (4 x $1.93)
BETA = 0.45
RF, ERP = 0.040, 0.050

# Forward estimates (consensus 2026/27; author model 2028-30)
rev   = {2025: 26.89, 2026: 28.15, 2027: 29.60, 2028: 31.20, 2029: 32.90, 2030: 34.70}
eps_a = {2025: 12.20, 2026: 12.93, 2027: 13.89, 2028: 15.10, 2029: 16.40, 2030: 17.85}
fcf   = {2025: 7.20, 2026: 7.60, 2027: 8.10, 2028: 8.70, 2029: 9.30, 2030: 9.90}

# ---------- WACC ----------
coe = RF + BETA * ERP
cod_at = 0.050 * (1 - 0.22)
E = PRICE * SHARES_M / 1000.0
wacc_capm = (E / (E + NET_DEBT_B)) * coe + (NET_DEBT_B / (E + NET_DEBT_B)) * cod_at
print(f"Market cap ${E:.1f}B | CoE {coe*100:.2f}% | after-tax CoD {cod_at*100:.2f}% | CAPM WACC {wacc_capm*100:.2f}%")

def dcf(wacc, g):
    pv = 0.0
    for i, y in enumerate([2026, 2027, 2028, 2029, 2030], start=1):
        pv += fcf[y] / (1 + wacc) ** i
    tv = fcf[2030] * (1 + g) / (wacc - g)
    pv += tv / (1 + wacc) ** 5
    eq = pv - NET_DEBT_B
    return pv, tv, eq, eq * 1000 / SHARES_M

print("\n--- DCF sensitivity (per share) ---")
print(f"{'WACC':>6} | " + " | ".join(f"g={g*100:.0f}%" for g in [0.025, 0.030, 0.035]))
for w in [0.060, 0.065, 0.070, 0.075, 0.080]:
    row = " | ".join(f"${dcf(w, g)[3]:7.0f}" for g in [0.025, 0.030, 0.035])
    print(f"{w*100:5.1f}% | {row}")

base_pv, base_tv, base_eq, base_px = dcf(0.065, 0.030)
print(f"\nBase DCF (WACC 6.5%, g 3.0%): EV ${base_pv:.1f}B, TV ${base_tv:.1f}B, equity ${base_eq:.1f}B -> ${base_px:.0f}/sh")

# ---------- Forward P/E ----------
print("\n--- Forward P/E (2027E EPS $13.89) ---")
for m in [18, 20, 22, 24, 26]:
    print(f"  {m}x -> ${m * eps_a[2027]:.0f}")
pe_base = 22 * eps_a[2027]
print(f"  Base 22x -> ${pe_base:.0f}")

# ---------- EV/EBITDA ----------
ebitda_27 = 15.9  # ~47% op margin on 29.6B rev + ~2.0B D&A
print(f"\n--- EV/EBITDA (2027E EBITDA ${ebitda_27}B) ---")
for m in [14, 15, 16.5, 18, 19]:
    ev = m * ebitda_27
    px = (ev - NET_DEBT_B) * 1000 / SHARES_M
    print(f"  {m}x -> EV ${ev:.0f}B -> ${px:.0f}/sh")
ev_base = 16.5 * ebitda_27
ev_px = (ev_base - NET_DEBT_B) * 1000 / SHARES_M

# ---------- Gordon DDM ----------
print("\n--- Dividend Discount Model ---")
def ddm(r, g):
    return DIV0 * (1 + g) / (r - g)
for r, g in [(0.085, 0.060), (0.090, 0.060), (0.095, 0.060), (0.090, 0.055), (0.090, 0.065)]:
    print(f"  r={r*100:.1f}%, g={g*100:.1f}% -> ${ddm(r, g):.0f}")
ddm_base = ddm(0.090, 0.060)

# ---------- Blend ----------
blend = 0.40 * base_px + 0.30 * pe_base + 0.20 * ev_px + 0.10 * ddm_base
print(f"\n=== BLEND: 40% DCF ${base_px:.0f} + 30% P/E ${pe_base:.0f} + 20% EV/EBITDA ${ev_px:.0f} + 10% DDM ${ddm_base:.0f} = ${blend:.0f} ===")
print(f"Upside from ${PRICE}: {(blend/PRICE-1)*100:.1f}%")

# ---------- Scenario targets ----------
print("\n--- Scenario price targets ---")
bull = 25 * 14.60   # re-rate to 25x on bull-case 2027 EPS
bear = 17 * 12.50   # de-rate to 17x on stalled EPS
print(f"Bull ${bull:.0f} | Base ${blend:.0f} | Bear ${bear:.0f}")
