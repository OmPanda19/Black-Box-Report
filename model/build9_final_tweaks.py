import openpyxl
wb = openpyxl.load_workbook('Black_Box_Co_Model.xlsx', data_only=False)

# Slightly more generous / consistent target multiples (fairness)
rel = wb['Relative']
rel['B19']=20   # bear P/E
rel['B20']=26   # base P/E
rel['B21']=32   # bull P/E
rel['D19']=11; rel['D20']=13; rel['D21']=16  # EV/EBITDA cases

summ = wb['Summary']
summ['B5']=13   # EV/EBITDA cross-check target (closer to WESCO ~13x; premium to peer median ~9.5x)

cov = wb['Cover']
cov['B14']='Relative (26x FY27E EPS, base)'

wb.save('Black_Box_Co_Model.xlsx')
print('Final multiple tweaks saved.')
