# -*- coding: utf-8 -*-
import openpyxl
from copy import copy
wb = openpyxl.load_workbook('Black_Box_Co_Model.xlsx', data_only=False)
cols=['D','E','F','G','H','I']  # FY27E..FY32E

# ============================================================
# FORECAST: tax normalisation to statutory, capex reclass, depreciation
# ============================================================
fc = wb['Forecast']
# Tax: normalise 12% -> 25% (statutory) as US/India NOLs deplete (audit Issue 4)
fc['A14']='Effective tax rate (NOL depletion -> statutory ~25%)'
taxr={'D':0.12,'E':0.15,'F':0.18,'G':0.21,'H':0.24,'I':0.25}
for c,v in taxr.items(): fc[f'{c}14']=v
# Capex: reclassify/reduce; label clarifies it INCLUDES ROU/lease & intangible additions
# (pure cash PP&E capex is ~0.7-1.0% of revenue per FY25 filings; balance is ROU/intangibles)
fc['A13']='Capex incl. ROU/lease & intangible additions (pure cash capex ~0.7-1.0%)'
capx={'D':0.013,'E':0.012,'F':0.012,'G':0.011,'H':0.011,'I':0.011}
for c,v in capx.items(): fc[f'{c}13']=v
# Depreciation: 12.5% of prior fixed assets (incl ROU amortisation) - keeps FA roll-forward stable
for c in cols: fc[f'{c}12']=0.125

# ============================================================
# DCF: moderate WACC, terminal growth, mid-year convention, sensitivity recentre
# ============================================================
dcf=wb['DCF']
dcf['A6']='Beta (small-cap integrator; moderated from 1.30 toward sector norms)'
dcf['B6']=1.10                              # Ke = 6.8% + 1.10*7.0% = 14.5%
dcf['A16']='Terminal growth rate (g) - long-run INR nominal (USD-centric, mature)'
dcf['B16']=0.05                             # 5% (audit Issue 6)
# Mid-year convention on discount factors
dcf['A32']='Discount factor @ WACC (mid-year convention)'
midyr={'B':0.5,'C':1.5,'D':2.5,'E':3.5,'F':4.5,'G':5.5}
for c,t in midyr.items():
    dcf[f'{c}32']=f'=1/(1+$B$13)^{t}'
# PV of terminal value discounted at mid-year of final period (5.5)
dcf['A37']='PV of terminal value (mid-year)'
dcf['C37']='=C36/(1+B13)^5.5'
# Sensitivity table recentred (WACC 12-15%, g 3-6%) with mid-year
gv={'B':0.03,'C':0.04,'D':0.045,'E':0.05,'F':0.06}
for c,v in gv.items():
    dcf[f'{c}50']=v; dcf[f'{c}50'].number_format='0.0%'
wv={51:0.12,52:0.125,53:0.13,54:0.135,55:0.14,56:0.145,57:0.15}
for r,v in wv.items():
    dcf[f'A{r}']=v; dcf[f'A{r}'].number_format='0.0%'
for r in wv:
    for c in ['B','C','D','E','F']:
        f=(f'=(SUMPRODUCT($B$31:$G$31,1/(1+$A{r})^{{0.5,1.5,2.5,3.5,4.5,5.5}})'
           f'+$G$31*(1+{c}$50)/($A{r}-{c}$50)/(1+$A{r})^5.5+$B$17)/$B$18')
        dcf[f'{c}{r}']=f; dcf[f'{c}{r}'].number_format='#,##0'

# ============================================================
# RELATIVE: expand peer set to span global economic peers + Indian listed tech/infra
# ============================================================
rel=wb['Relative']
peers=[
 ('WESCO International (US distr. + DC deploy)',22,13),
 ('Kyndryl (US managed infra svcs; turnaround)',30,5.5),
 ('Redington (India IT distribution/infra)',16,9),
 ('Tata Communications (India digital infra)',38,9),
 ('Mastek (India IT services - mid cap)',16,8),
 ('Happiest Minds (India digital/IT)',38,19),
]
r=5
for name,pe,ev in peers:
    rel[f'A{r}']=name
    rel[f'L{r}']=pe; rel[f'L{r}'].number_format='0.0'
    rel[f'M{r}']=ev; rel[f'M{r}'].number_format='0.0'
    for cc in ['B','C','D','E','F','G','H','I','J','K']:
        rel[f'{cc}{r}']=None
    r+=1
rel['A23']=('Note: Peer set spans BB\'s closest economic analogs (WESCO, Kyndryl, Redington - low-margin '
'integration/distribution/managed svcs) and Indian listed tech/infra (Tata Comm, Mastek, Happiest Minds). '
'Peer median P/E ~26x, EV/EBITDA ~9x. Black Box at ~46x FY27E / ~65x trailing remains a clear premium; '
'target multiples set at ~peer median (base 26x), a large discount to BBOX\'s current multiple. '
'Multiples approximate (~Aug-2026) - refresh with live data.')

# ============================================================
# SUMMARY: EV/EBITDA target aligned to refreshed peer median
# ============================================================
wb['Summary']['B5']=12   # closer to peer median EV/EBITDA ~9x, modest growth premium

# ============================================================
# OPERATING DRIVERS: explicit contract accounting (audit Issue 3)
# ============================================================
od=wb['Operating Drivers']
red=copy(od['A3'].font)
od['A38']='SECTION 7 — CONTRACT ACCOUNTING (Ind-AS 115) - INR cr'; od['A38'].font=copy(red)
# columns G..L = FY21..FY26
ca={'G':0,'H':44,'I':114,'J':246,'K':219,'L':280}       # contract assets (unbilled)
cl={'G':0,'H':523,'I':560,'J':555,'K':500,'L':576}      # contract liabilities (deferred rev, curr+NC)
od['A39']='Contract Assets (unbilled revenue)'
od['A40']='Contract Liabilities (deferred revenue/advances)'
for c,v in ca.items(): od[f'{c}39']=v; od[f'{c}39'].number_format='#,##0'
for c,v in cl.items(): od[f'{c}40']=v; od[f'{c}40'].number_format='#,##0'
# forecast (M..R) scale contract liab/assets with revenue (as in Forecast WC via other CA/CL)
od['M39']='scaled w/ revenue in Forecast (other CA)'; od['M40']='scaled w/ revenue in Forecast (other CL)'

# ============================================================
# COVER: update valuation labels
# ============================================================
cov=wb['Cover']
cov['B13']='DCF (intrinsic; WACC ~13.9%, g 5%, mid-year)'

# ============================================================
# ASSUMPTIONS: update changed drivers + reconciliation note
# ============================================================
asm=wb['Assumptions']
def putrow(r,a,b,c,d,e,f,g,h,i):
    for col,v in zip('ABCDEFGHI',[a,b,c,d,e,f,g,h,i]): asm[f'{col}{r}']=v
putrow(16,'Effective tax rate',
 'Normalises 12% (FY27E) -> 25% (FY32E, statutory)',
 'Reported ~3-10% (NOL-shielded)',
 'US + India NOLs deplete; converges to blended statutory ~25%',
 'Not explicitly guided',
 'India 25%, US ~21-25%',
 'AUDIT-DRIVEN: normalised toward statutory (best practice for terminal); conservative vs low reported rate',
 'Medium','Filings; independent judgement')
putrow(23,'Capex (incl. ROU/lease & intangible additions)',
 '~1.1-1.3% of revenue',
 'Pure cash capex ~0.7-1.0% (FY25 Rs44cr=0.7%); + ROU/intangible additions',
 'Ind-AS 116 leases: depreciation incl ROU amortisation, so investment line incl lease/intangible additions',
 'Mgmt: asset-light',
 'n/a',
 'AUDIT-DRIVEN: reduced & reclassified; pure cash capex low, balance is ROU/intangibles to keep FA roll-forward consistent',
 'Medium','FY25 cash flow; independent judgement')
putrow(29,'Beta','1.10 (moderated from 1.30)','Small-cap, cyclical, promoter overhang','Sector integrator betas ~0.9-1.2','n/a','Auto ~0.95','AUDIT-DRIVEN: moderated toward sector norms; Ke = 6.8% + 1.10x7.0% = 14.5%','Medium','Independent judgement')
putrow(30,'WACC','~13.9% (was 15.2%)','Ke 14.5%; after-tax Kd ~7.3%; weights 92/8','Moved toward institutional norms (audit 11-13%)','n/a','India small/mid-cap DCFs 12-14%','AUDIT-DRIVEN: moderated; still a modest risk premium for size/governance','High','DCF sheet')
putrow(31,'Terminal growth','5.0% (was 6%)','~4% USD nominal + INR depreciation','Below India nominal GDP; USD-centric mature integrator','n/a','Mature-franchise terminal','AUDIT-DRIVEN: lowered to conservative 5%; mid-year convention added','Medium','Independent judgement')
putrow(35,'Peer set',
 'WESCO, Kyndryl, Redington, Tata Comm, Mastek, Happiest Minds',
 'Peer median P/E ~26x, EV/EBITDA ~9x; BB ~46-65x',
 'AUDIT-DRIVEN: spans global economic analogs + Indian listed tech/infra',
 'n/a','Tata Comm/Mastek/Happiest Minds add Indian context',
 'Balanced set on business economics & listing market; BB a clear premium',
 'Medium-High','Yahoo/BSE/company - Aug-2026 (approx; refresh)')
# Reconciliation note re: rejected audit "corrections"
asm['A44']='Audit reconciliation - FY25 figures'
asm['B44']='FY25 (Mar-25) consol: Revenue 5,967; PBT 212; PAT 205; equity 759; borrowings 654'
asm['C44']='Confirmed by audited FY24-25 Annual Report MD&A (Directors Report p.94-95)'
asm['D44']='The DD note\'s "FY25 PAT 137.67 / PBT 156.39 / borrowings 397" are the FY24 (Mar-24) figures'
asm['E44']='n/a'; asm['F44']='n/a'
asm['G44']='REJECTED those "corrections" - they would replace correct FY25 audited values with FY24; model already matches audited AR'
asm['H44']='High'; asm['I44']='Annual Report FY24-25 MD&A; Investor Pres p.22'

wb.calculation.fullCalcOnLoad=True
wb.save('Black_Box_Co_Model.xlsx')
print('Audit-response changes applied & saved.')
