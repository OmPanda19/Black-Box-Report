import openpyxl
from copy import copy
wb = openpyxl.load_workbook('Black_Box_Co_Model.xlsx', data_only=False)
ws = wb['Relative']

hdr_font = copy(ws['A3'].font)
# clear A3:M21
for r in range(3,22):
    for cc in range(1,14):
        ws.cell(row=r, column=cc).value=None

ws['A1']='BLACK BOX LTD - RELATIVE VALUATION (economic peers: infra integrators/distributors)'

# Header row
heads=['Company','Price (local)','Mkt Cap','Net debt/(cash)','EV','Revenue','EBITDA','PAT','EPS','ROE','ROCE','P/E','EV/EBITDA']
for i,h in enumerate(heads):
    c=ws.cell(row=3,column=1+i); c.value=h; c.font=copy(hdr_font)

# Subject: Black Box (INR cr)
ws['A4']='Black Box (subject)'
ws['B4']='=Cover!C6'
ws['C4']='=B4*DCF!B18'                # mkt cap
ws['D4']=287                          # net debt
ws['E4']='=C4+D4'                     # EV
ws['F4']='=Historicals!K6'            # revenue
ws['G4']='=Forecast!C51'              # FY26 EBITDA (clean)
ws['H4']='=Historicals!K30'           # PAT
ws['I4']='=Historicals!K33'           # EPS
ws['J4']='=Historicals!K30/AVERAGE(Historicals!J46,Historicals!K46)'   # ROE
ws['K4']='=(Historicals!K22+Historicals!K16)/(Historicals!K46+Historicals!K49+Historicals!K55)'  # ROCE
ws['L4']='=C4/H4'                     # P/E
ws['M4']='=E4/G4'                     # EV/EBITDA
for a in ['B4','C4','D4','E4','F4','G4','H4']: ws[a].number_format='#,##0'
ws['L4'].number_format='0.0'; ws['M4'].number_format='0.0'; ws['J4'].number_format='0.0%'; ws['K4'].number_format='0.0%'

# Peers (approximate current multiples, ~Aug-2026 - VERIFY/refresh with live data)
peers=[
 ('WESCO International (US distr. + DC deploy)',22,13),
 ('Insight Enterprises (US IT integrator)',15,10),
 ('Kyndryl (US managed infra svcs; turnaround)',30,5.5),
 ('Redington (India IT distribution/infra)',16,9),
 ('HCLTech (India IT svcs - quality ref.)',19,12),
 ('Allied Digital (India IT infra SI)',13,8),
]
r=5
for name,pe,ev in peers:
    ws[f'A{r}']=name
    ws[f'L{r}']=pe; ws[f'L{r}'].number_format='0.0'
    ws[f'M{r}']=ev; ws[f'M{r}'].number_format='0.0'
    r+=1
# stats
ws['A11']='Peer median (economic peers)'; ws['L11']='=MEDIAN(L5:L10)'; ws['M11']='=MEDIAN(M5:M10)'
ws['A12']='Peer mean'; ws['L12']='=AVERAGE(L5:L10)'; ws['M12']='=AVERAGE(M5:M10)'
for a in ['L11','L12','M11','M12']: ws[a].number_format='0.0'

# Target multiple application (KEEP outputs at F19/F20/F21 for Summary/Cover links)
ws['A13']='TARGET PRICE — MULTIPLE APPLICATION'; ws['A13'].font=copy(hdr_font)
ws['A14']='Black Box FY27E EPS (consol PAT / shares)'; ws['B14']='=Forecast!D49'; ws['B14'].number_format='0.0'
ws['A15']='Black Box FY28E EPS'; ws['B15']='=Forecast!E49'; ws['B15'].number_format='0.0'
ws['A16']='Black Box FY27E EBITDA (INR cr)'; ws['B16']='=Forecast!D51'; ws['B16'].number_format='#,##0'
ws['A18']='Case'; ws['B18']='Target P/E'; ws['C18']='Implied TP (P/E x FY27E EPS)'
ws['D18']='Target EV/EBITDA'; ws['E18']='Implied TP (EV/EBITDA)'; ws['F18']='Relative TP (P/E-based)'
for cc in ['A18','B18','C18','D18','E18','F18']: ws[cc].font=copy(hdr_font)
cases=[(19,'Bear (low)',18,12),(20,'Base',25,15),(21,'Bull (high)',32,18)]
for row,label,pe,ev in cases:
    ws[f'A{row}']=label
    ws[f'B{row}']=pe
    ws[f'C{row}']=f'=B{row}*$B$14'
    ws[f'D{row}']=ev
    ws[f'E{row}']=f'=(D{row}*$B$16-DCF!$B$17*-1+DCF!$B$17)/DCF!$B$18'  # EV -> equity: (EV/EBITDA*EBITDA + netcash)/shares ; netcash=DCF!B17
    ws[f'E{row}']=f'=(D{row}*$B$16+DCF!$B$17)/DCF!$B$18'
    ws[f'F{row}']=f'=C{row}'
    for a in [f'C{row}',f'E{row}',f'F{row}']: ws[a].number_format='#,##0'

ws['A23']='Note: Peer P/E & EV/EBITDA are approximate (~Aug-2026) and should be refreshed with live data. Black Box trades at ~3-4x the P/E of its true economic peers (WESCO ~22x, Redington ~16x, Kyndryl ~5.5x EV/EBITDA); target multiples set at a growth premium to peers but a large discount to BBOXs current ~65-70x.'

wb.save('Black_Box_Co_Model.xlsx')
print('Relative rebuilt & saved.')
