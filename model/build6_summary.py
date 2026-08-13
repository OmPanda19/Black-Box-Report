import openpyxl
from copy import copy
wb = openpyxl.load_workbook('Black_Box_Co_Model.xlsx', data_only=False)
ws = wb['Summary']

ws['A1']='BLACK BOX LTD - VALUATION SUMMARY'
# clear old SOTP block A3:B14 (skip merged cells)
from openpyxl.cell.cell import MergedCell
for r in range(3,15):
    for cc in range(1,9):
        cell = ws.cell(row=r, column=cc)
        if not isinstance(cell, MergedCell):
            cell.value=None

sec_font = copy(ws['A22'].font) if ws['A22'].font else None

ws['A3']='VALUATION METHOD 3 — EV/EBITDA CROSS-CHECK'
ws['A4']='FY27E EBITDA (INR cr)';           ws['B4']='=Forecast!D51'; ws['B4'].number_format='#,##0'
ws['A5']='Target EV/EBITDA (x)';            ws['B5']=15; ws['B5'].number_format='0.0'
ws['A6']='Implied Enterprise Value';        ws['B6']='=B4*B5'; ws['B6'].number_format='#,##0'
ws['A7']='Add: net cash / (less net debt)'; ws['B7']='=DCF!B17'; ws['B7'].number_format='#,##0'
ws['A8']='Implied Equity Value';            ws['B8']='=B6+B7'; ws['B8'].number_format='#,##0'
ws['A9']='Shares outstanding (cr)';         ws['B9']='=DCF!B18'; ws['B9'].number_format='0.0'
ws['A10']='EV/EBITDA-based TP (INR/share)'; ws['B10']='=B8/B9'; ws['B10'].number_format='#,##0'
ws['A14']='EV/EBITDA cross-check TP (INR/share)'; ws['B14']='=B10'; ws['B14'].number_format='#,##0'

ws['A16']='BLENDED TARGET PRICE (weighted base)'; ws['B16']='=SUMPRODUCT(C24:C26,E24:E26)'; ws['B16'].number_format='#,##0'
ws['A17']='Current price (INR)';   ws['B17']='=DCF!B19'; ws['B17'].number_format='#,##0'
ws['A18']='Upside / (downside) vs current'; ws['B18']='=B16/B17-1'; ws['B18'].number_format='0.0%'
ws['A19']='Recommendation'; ws['B19']='=IF(B18>0.15,"BUY",IF(B18>0,"ACCUMULATE",IF(B18>-0.1,"NEUTRAL/HOLD","REDUCE")))'

ws['A22']='VALUATION SUMMARY — METHOD TRIANGULATION, BLENDED TARGET & RECOMMENDATION'
ws['A23']='Method'; ws['B23']='Bear'; ws['C23']='Base'; ws['D23']='Bull'; ws['E23']='Weight'
ws['A24']='DCF (FCFF; WACC 13-16%, g 4-6.5%)'
ws['B24']='=DCF!B57'    # high WACC, low g corner (bear)
ws['C24']='=DCF!C41'    # base
ws['D24']='=DCF!F51'    # low WACC, high g corner (bull)
ws['E24']=0.40
ws['A25']='Relative (P/E on FY27E EPS)'
ws['B25']='=Relative!F19'; ws['C25']='=Relative!F20'; ws['D25']='=Relative!F21'; ws['E25']=0.40
ws['A26']='EV/EBITDA cross-check'
ws['C26']='=B10'; ws['E26']=0.20
for a in ['B24','C24','D24','B25','C25','D25','C26']: ws[a].number_format='#,##0'
for a in ['E24','E25','E26']: ws[a].number_format='0%'

wb.save('Black_Box_Co_Model.xlsx')
print('Summary rebuilt & saved.')
