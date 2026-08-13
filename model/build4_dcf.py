import openpyxl
wb = openpyxl.load_workbook('Black_Box_Co_Model.xlsx', data_only=False)
ws = wb['DCF']

# WACC build-up
ws['A4']='Risk-free rate (India 10Y G-sec, ~Jun-2026)'; ws['B4']=0.068
ws['A5']='Equity risk premium (India)'; ws['B5']=0.070
ws['A6']='Beta (small-cap digital-infra integrator, incl. size/specific risk)'; ws['B6']=1.30
ws['B7']='=B4+B6*B5'                      # cost of equity ~15.9%
ws['A8']='Pre-tax cost of debt (blended, incl leases)'; ws['B8']='=AVERAGE(Forecast!D11:I11)'
ws['B9']='=AVERAGE(Forecast!D14:I14)'     # avg tax
ws['B10']='=B8*(1-B9)'
ws['A11']='Equity weight'; ws['B11']=0.92
ws['B12']='=1-B11'
ws['B13']='=(B11*B7)+(B12*B10)'           # WACC ~15.1%

# Terminal / bridge
ws['A16']='Terminal growth rate (g) — long-run INR nominal (mature global integrator)'; ws['B16']=0.06
ws['A17']='Net (debt) / cash [FY26A: borrowings 827 + ST 30 lease-adj - cash 540 ~ (287)]'; ws['B17']=-287
ws['A18']='Shares outstanding (cr)'; ws['B18']=18.0
ws['A19']='Current market price (INR) [links Cover]'; ws['B19']='=Cover!C6'

# FCFF cleanup — remove NBFC finance adjustment
ws['A23']='EBIT (= PBT + finance cost)'
ws['A24']='Less: non-operating adjustment (n/a for Black Box)'
for c in ['B','C','D','E','F','G']:
    ws[f'{c}24']=0

# Sensitivity table (explicit formulas, replacing Excel DataTable)
ws['A47']='BLACK BOX LTD - SENSITIVITY ANALYSIS'
ws['A49']='DCF TARGET PRICE (INR): WACC (rows) vs TERMINAL GROWTH (cols)'
ws['A50']='=C41'
g_vals = {'B':0.04,'C':0.05,'D':0.055,'E':0.06,'F':0.065}
for c,v in g_vals.items():
    ws[f'{c}50']=v; ws[f'{c}50'].number_format='0.0%'
wacc_vals = {51:0.13,52:0.135,53:0.14,54:0.145,55:0.15,56:0.155,57:0.16}
for r,v in wacc_vals.items():
    ws[f'A{r}']=v; ws[f'A{r}'].number_format='0.0%'
for r in wacc_vals:
    for c in ['B','C','D','E','F']:
        f=(f'=(SUMPRODUCT($B$31:$G$31,1/(1+$A{r})^{{1,2,3,4,5,6}})'
           f'+$G$31*(1+{c}$50)/($A{r}-{c}$50)/(1+$A{r})^6+$B$17)/$B$18')
        ws[f'{c}{r}']=f
        ws[f'{c}{r}'].number_format='#,##0'

wb.save('Black_Box_Co_Model.xlsx')
print('DCF rebuilt & saved.')
