import formulas, warnings, logging, openpyxl
warnings.filterwarnings('ignore'); logging.getLogger('formulas').setLevel(logging.CRITICAL)

# 1) Error-string scan across saved workbook (openpyxl formulas won't show #REF unless cached; scan values)
wbv = openpyxl.load_workbook('Black_Box_Co_Model.xlsx', data_only=False)
errs=[]
for ws in wbv.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value,str) and c.value.startswith('=') and ('#REF' in c.value or '#DIV' in c.value or '#VALUE' in c.value):
                errs.append((ws.title,c.coordinate,c.value))
print("Formula error strings found:", len(errs))
for e in errs[:20]: print("  ",e)

# 2) Recalculate
xl = formulas.ExcelModel().loads('Black_Box_Co_Model.xlsx').finish()
sol = xl.calculate()
FN="'[Black_Box_Co_Model.xlsx]"
def g(sheet,cell):
    try:
        v=sol[f"{FN}{sheet.upper()}'!{cell}"].value
        try: return float(v[0,0])
        except Exception:
            try: return v[0,0]
            except Exception: return v
    except Exception as ex: return f"ERR:{ex}"

print("\n=== HISTORICALS balance (TotalAssets K81 vs TotalCap&Liab K60) ===")
for y,c in [('FY21','F'),('FY22','G'),('FY23','H'),('FY24','I'),('FY25','J'),('FY26','K')]:
    ta=g('HISTORICALS',f'{c}81'); tl=g('HISTORICALS',f'{c}60')
    print(f" {y}: assets={round(ta)} liab={round(tl)} diff={round(ta-tl,3)}")

print("\n=== FORECAST FCFF (DCF) ===")
for c in ['B','C','D','E','F','G']:
    print(f"  {c}: EBIT={round(g('DCF',c+'23'))} NOPAT={round(g('DCF',c+'27'))} FCFF={round(g('DCF',c+'31'))}")

print("\n=== DCF sensitivity table (rows WACC, cols g) ===")
gs=[g('DCF',f'{c}50') for c in ['B','C','D','E','F']]
print("   g:", [round(x,3) for x in gs])
for r in range(51,58):
    w=g('DCF',f'A{r}')
    vals=[round(g('DCF',f'{c}{r}')) for c in ['B','C','D','E','F']]
    print(f"  WACC {round(w,3)}: {vals}")

print("\n=== FINAL VALUATION ===")
print(" DCF TP:", round(g('DCF','C41')))
print(" Relative bear/base/bull:", round(g('RELATIVE','F19')), round(g('RELATIVE','F20')), round(g('RELATIVE','F21')))
print(" EV/EBITDA TP:", round(g('SUMMARY','B10')))
print(" Blended target:", round(g('SUMMARY','B16')), " Upside:", round(g('SUMMARY','B18')*100,1),"%  Reco:", g('SUMMARY','B19'))
print(" Cover target/upside/reco:", round(g('COVER','C7')), round(g('COVER','C8')*100,1), g('COVER','C5'))
print(" FY27E EPS:", round(g('FORECAST','D49'),1), " FY27 P/E at price:", round(g('COVER','C6')/g('FORECAST','D49'),1))
