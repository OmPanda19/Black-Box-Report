import formulas, warnings, logging
warnings.filterwarnings('ignore'); logging.getLogger('formulas').setLevel(logging.CRITICAL)
xl = formulas.ExcelModel().loads('Black_Box_Co_Model.xlsx').finish()
sol = xl.calculate()

FN = "'[Black_Box_Co_Model.xlsx]"
def g(sheet, cell):
    key = f"{FN}{sheet.upper()}'!{cell}"
    try:
        v = sol[key].value
        try: return float(v[0,0])
        except Exception:
            try: return v[0,0]
            except Exception: return v
    except Exception as e:
        return f"ERR:{e}"

print("=== FORECAST checks (should be ~0) ===")
for c in ['D','E','F','G','H','I']:
    print(f" {c} balance(111)=", round(g('FORECAST',f'{c}111'),4), " cash-tie(112)=", round(g('FORECAST',f'{c}112'),4))

print("\n=== FORECAST P&L path ===")
yrs=['FY27','FY28','FY29','FY30','FY31','FY32']; cols=['D','E','F','G','H','I']
print(" Revenue:", [round(g('FORECAST',f'{c}30')) for c in cols])
print(" EBITDA :", [round(g('FORECAST',f'{c}51')) for c in cols])
print(" EBITDAm:", [round(g('FORECAST',f'{c}52')*100,1) for c in cols])
print(" PAT    :", [round(g('FORECAST',f'{c}46')) for c in cols])
print(" EPS    :", [round(g('FORECAST',f'{c}49'),1) for c in cols])
print(" FY26A rev/ebitda/pat:", round(g('FORECAST','C30')), round(g('FORECAST','C51')), round(g('FORECAST','C46')))

print("\n=== DCF ===")
for lbl,cell in [('Ke','B7'),('WACC','B13'),('SumPV','C35'),('TV','C36'),('PV_TV','C37'),('EV','C38'),('Equity','C40'),('TP','C41'),('Upside','C43'),('TV%EV','C44')]:
    print(f" {lbl:8}=", g('DCF',cell))

print("\n=== RELATIVE ===")
print(" Subject P/E:", g('RELATIVE','L4'), " EV/EBITDA:", g('RELATIVE','M4'))
print(" Peer median P/E:", g('RELATIVE','L11'), " EV/EBITDA:", g('RELATIVE','M11'))
print(" Rel TP bear/base/bull:", g('RELATIVE','F19'), g('RELATIVE','F20'), g('RELATIVE','F21'))

print("\n=== SUMMARY ===")
print(" EV/EBITDA TP:", g('SUMMARY','B10'))
print(" Blended target:", g('SUMMARY','B16'), " Upside:", g('SUMMARY','B18'), " Reco:", g('SUMMARY','B19'))
print(" Triangulation DCF b/base/bull:", g('SUMMARY','B24'), g('SUMMARY','C24'), g('SUMMARY','D24'))

print("\n=== COVER ===")
print(" Target(C7):", g('COVER','C7'), " Upside(C8):", g('COVER','C8'), " Reco(C5):", g('COVER','C5'))
