import openpyxl
wb = openpyxl.load_workbook('Black_Box_Co_Model.xlsx', data_only=False)

fc = wb['Forecast']
# Effective finance charge on modeled borrowing line (captures lease interest + normalised FX,
# since the borrowing line excludes ~Rs326cr lease liabilities)
fc['A11']='Effective finance cost on borrowings (incl. lease interest & normalised FX)'
fc['D11']=0.155
for c in ['E','F','G','H','I']:
    prev={'E':'D','F':'E','G':'F','H':'G','I':'H'}[c]
    fc[f'{c}11']=f'={prev}11'

# Exceptional items (positive = loss; forecast row44 = row42 - row43). Mgmt flagged 2-3 more
# quarters of restructuring/severance into FY27, tapering.
fc['A43']='Exceptional Items (restructuring/severance - tapering)'
exc={'D':90,'E':50,'F':20,'G':0,'H':0,'I':0}
for c,v in exc.items():
    fc[f'{c}43']=v
    fc[f'{c}43'].number_format='#,##0'

dcf = wb['DCF']
# Use TRUE marginal borrowing cost for WACC (not the effective P&L charge)
dcf['A8']='Pre-tax cost of debt (marginal borrowing rate)'
dcf['B8']=0.09

wb.save('Black_Box_Co_Model.xlsx')
print('Fixes applied & saved.')
