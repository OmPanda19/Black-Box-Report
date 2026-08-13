# -*- coding: utf-8 -*-
import openpyxl
wb = openpyxl.load_workbook('Black_Box_Co_Model.xlsx', data_only=False)

# ================= COVER =================
cv = wb['Cover']
cv['A1']='BLACK BOX LTD - INVESTMENT SUMMARY'
cv['A2']='NSE: BBOX  |  BSE: 500463  |  Sector: Digital Infrastructure / Enterprise Networking & Systems Integration'
cv['B6']='Current Price (INR, ~12-Aug-2026)'
cv['B13']='DCF (intrinsic; WACC ~15.1%, g 6%)'
cv['B14']='Relative (25x FY27E EPS, base)'
cv['B15']='EV/EBITDA cross-check (15x FY27E)'
cv['B17']='Street coverage: thin (2-3 analysts); MF ownership ~0%'

cv['B20']=("The market treats Black Box as a de-risked Indian proxy for the global AI / data-centre infrastructure "
"build-out and prices it at ~50-70x trailing earnings on the promise of a US$2bn-by-FY30 revenue plan. My research "
"suggests the business, though genuinely turned around (EBITDA margin ~4%->9%, net worth negative->Rs1,287cr), remains "
"a thin-margin (~9%), cash-light, no-pricing-power systems integrator with high customer/geographic concentration, a "
"heavy Essar/Ruia promoter overhang and a growth plan already running behind its own timeline (FY26 revenue guidance cut; "
"US$2bn target slipped FY29->FY30). At the current price there is little margin of safety.")

cv['B23']='Pillar 1 - Genuine operational turnaround, but now fully priced'
cv['B24']=("From a distressed, negative-net-worth 2019 merger, BB lifted EBITDA margin from ~4% (FY23) to ~9% (FY26), "
"repaired the balance sheet and built a US$949mn backlog with 20-year Fortune-500 relationships (Bank of America the largest). "
"The improvement is real and largely structural - but the equity already capitalises it at a premium to global peers.")
cv['B25']='Pillar 2 - AI/data-centre exposure is real but indirect, thin-margin and input-constrained'
cv['B26']=("BB sells deployment labour, fibre and cabling into hyperscaler builds (DC mix 17%->~30%), not compute/GPUs, and "
"wins on technical merit, not price. FY26 showed backlog can be delayed by fibre/GPU/power shortages outside BB's control. "
"It is a participant in the capex wave, not a driver, and a tiny slice of each customer's budget.")
cv['B27']='Pillar 3 - Earnings quality and cash conversion are the swing factors the market underweights'
cv['B28']=("Reported PAT is flattered by a ~8-10% NOL-driven tax rate (normalising to ~18-20% in the model) and by excluding "
"7+ quarters of 'exceptionals'; revenue was ~flat at ~Rs6,000cr for four years and free cash flow is weak/volatile "
"(CFO negative in FY25) as growth consumes ~0.2-0.3x working capital. The US$2bn plan leans on ~Rs6,000cr of unproven serial M&A.")

cv['B30']='KEY CATALYSTS (+)'; cv['E30']='KEY RISKS (-)'
cv['B31']='- Sustained order booking >US$300-350mn/quarter'; cv['E31']='- Premium multiple (~50-70x) => de-rating risk; little margin of safety'
cv['B32']='- Repeatable hyperscaler DC wins with annuity tails'; cv['E32']='- Guidance-delivery risk (FY26 cut; FY30 target slipped a year)'
cv['B33']='- EBITDA margin crossing 10%; exceptionals ending'; cv['E33']='- Weak/volatile FCF; receivables spike (DSO ~67 in FY26)'
cv['B34']='- Cross-sell into 20-yr Fortune-500 base; managed-services attach'; cv['E34']='- Customer concentration (top 10 ~51%; Bank of America largest)'
cv['B35']='- First clean FCF-positive year; institutional/MF entry'; cv['E35']='- Promoter/governance overhang (Essar/Ruia); tax normalisation'
cv['B36']='- Accretive, disciplined M&A (2S-style)'; cv['E36']='- FX (94% non-INR revenue); supply-chain (fibre/GPU/power)'

cv['B38']='DETAILED INVESTMENT VIEW'
cv['B39']=("Black Box has earned respect for execution: a small Indian company (AGC Networks) acquired the distressed, larger "
"US-listed Black Box Corporation for ~US$17mn of equity in 2019 and turned it into a ~Rs6,300cr, ~9% EBITDA-margin global "
"integrator with an enviable, sticky Fortune-500 client base. The FY26 backlog (US$792mn->US$949mn by Q1FY27) and the DC pivot "
"give a credible growth narrative. But three facts temper enthusiasm: revenue was essentially flat FY22-FY26; free cash flow "
"has been thin and often negative; and reported profit is flattered by a temporary tax rate and recurring 'exceptionals'.")
cv['B40']=("The valuation is built bottom-up across three methods. The DCF is the disciplined anchor: with Rf 6.8%, ERP 7.0% and "
"a small-cap/specific-risk beta of ~1.30, cost of equity is ~15.9% and WACC ~15.1% (materially above the auto-template's 12.7% "
"because BB is a smaller, riskier, promoter-controlled, cyclical name); at 6% terminal growth the FY27E-FY32E free cash flows "
"discount to an intrinsic value well below the current price - i.e., today's price already embeds success.")
cv['B41']=("Relative valuation is where the mispricing is clearest. BB's true economic peers - WESCO (~22x P/E), Insight (~15x), "
"Kyndryl (~5.5x EV/EBITDA), Redington (~16x), HCLTech (~19x), Allied Digital (~13x) - trade at a fraction of BB's ~65-70x. "
"Even a generous 25x base target on FY27E EPS (a premium to peers for growth/DC exposure) sits far below the current multiple, "
"implying limited-to-negative upside. The EV/EBITDA cross-check (15x FY27E EBITDA) corroborates.")
cv['B42']=("Triangulating DCF (40%), Relative (40%) and EV/EBITDA (20%) yields the blended target on the Summary sheet. The core "
"thesis on why the market is mispricing the stock: it is extrapolating a thematic AI/DC narrative onto a thin-margin, cash-light "
"integrator whose organic growth is unproven over a cycle, whose earnings quality is flattered, and whose promoter carries a "
"heavy governance legacy - none of which supports a multiple that prices flawless execution as a certainty.")
cv['B43']=("Return profile: base case tracks the blended target (see Summary); bull case requires sustained ~20% organic growth, "
"margins >10.5% and clean FCF (justifying a higher multiple); bear case (AI-capex digestion, dilutive raise, governance event, "
"tax normalisation) implies a >50% de-rating. The skew from today's price is unfavourable - downside to a DCF floor well below "
"price against limited upside unless the aggressive plan is delivered.")
cv['B45']='INSTITUTIONAL CONCLUSION'
cv['B46']=("We initiate with a cautious stance: NEUTRAL-to-underweight on the equity (constructive on the business, cautious on "
"the stock). Black Box is a much-improved, blue-chip-anchored integrator riding a genuine capex super-cycle, but at ~50-70x "
"earnings, with thin margins, weak cash conversion, high concentration and a promoter overhang, the risk/reward at the current "
"price is unattractive. We would turn constructive on a meaningful de-rating or on 2+ quarters of proven organic growth and "
"positive free cash flow. See Summary sheet for the model-derived blended target and recommendation.")

# ================= ASSUMPTIONS =================
asm = wb['Assumptions']
asm['A1']='BLACK BOX LTD - DETAILED ASSUMPTIONS & RESEARCH SUPPORT'
asm['A2']='A. REVENUE & GROWTH DRIVERS'
asm['A10']='B. MARGINS, COSTS & TAX'
asm['A19']='C. WORKING CAPITAL, CAPEX & BALANCE SHEET'
asm['A25']='D. DCF / WACC & TERMINAL VALUE'
asm['A33']='E. RELATIVE VALUATION'
asm['A39']='F. EV/EBITDA CROSS-CHECK, BLEND & RECOMMENDATION'

def putrow(r, a,b,c,d,e,f,g,h,i):
    vals={'A':a,'B':b,'C':c,'D':d,'E':e,'F':f,'G':g,'H':h,'I':i}
    for col,v in vals.items():
        asm[f'{col}{r}']=v

# A. Revenue & growth
putrow(4,'Organic revenue growth %',
 'FY27E +13% tapering to +9% by FY32E',
 'Revenue ~flat at ~Rs6,000cr FY22-26 (FY24 6,282 -> FY26 6,322); FY26 +6%',
 'AI/DC capex supercycle (global DC capex ~$430bn 2024 -> ~$1.1tn 2029); enterprise refresh',
 'Mgmt targets US$1.3bn organic (~17% CAGR) within US$2bn-by-FY30 plan',
 'WESCO/Anixter, Kyndryl in same layer',
 'Set BELOW mgmt implied ~17% - reflects unproven organic track record & backlog-conversion risk; top value driver',
 'Medium','BB Q1FY27 pres; industry (NetworkWorld/IDC) - 2026')
putrow(5,'Inorganic (acquired) revenue',
 'Rs500cr FY27 (2S Brazil) then Rs200-400cr/yr; ~Rs2,100cr cumulative',
 'First sizeable M&A = 2S (Brazil), ~Rs500cr, ~5-5.5x EBITDA',
 'Fragmented integrator market enables bolt-ons',
 'Mgmt aspires ~Rs6,000cr (US$700mn) inorganic by FY30',
 'Serial acquirers (WESCO) as model',
 'Modelled WELL BELOW ~Rs6,000cr aspiration - serial M&A unproven at scale; execution/integration risk',
 'Low-Medium','BB Q3FY26 call; Q1FY27 pres - 2026')
putrow(6,'Segment mix (GSI / TPS / Other)',
 'GSI ~84% / TPS ~14% / Other ~2% (held ~stable)',
 'FY26 disclosed 84/14/2',
 'GSI = services (DC, connectivity, networking, workplace, cyber); TPS = KVM/AV products',
 'Mgmt: GSI is the growth engine',
 'n/a','Mix stable; TPS higher-margin, GSI faster-growing (offset)',
 'Medium','BB FY26 pres p.26-27')
putrow(7,'Data-centre revenue mix %',
 '17% (FY26) -> ~30% (FY27E)',
 'DC ~17% of FY26',
 'Hyperscaler capex $600-900bn 2026; each GW needs fibre/cabling/deploy',
 'Mgmt guides DC ~30% of FY27',
 'WESCO DC momentum',
 'Rising DC mix is LOWER gross margin than products/managed svcs - a margin headwind, not tailwind',
 'Medium','BB Q1FY27 pres')
putrow(8,'Managed services / recurring %',
 '~30%+ of revenue (rising)',
 '>30% by FY25/FY26',
 'Day-2 annuity attach on projects ~10-15%',
 'Mgmt: converting projects to annuities (airports, healthcare, hyperscaler)',
 'n/a','Higher recurring mix improves visibility & multiple quality - key positive to monitor',
 'Medium','BB FY25 AR; calls')
putrow(9,'Geographic mix',
 'NA ~69%, EU ~9%, APAC ~8%, India ~6%, LatAm ~6%, MEA ~2%',
 'NA-centric since 2019 Black Box Corp deal',
 'US AI/DC build-out concentrated; India margin-dilutive',
 'Mgmt scaling Europe/India/LatAm (2S)',
 'n/a','94% non-INR => FX exposure; NA drives profit; India deliberately cautious on margin',
 'Medium','BB Q1FY27 pres')

# B. Margins, costs, tax
putrow(12,'Cost of revenue % (gross margin)',
 '~69.5% cost (gross margin ~30.5% -> 30.9%)',
 'Gross margin 26% (FY23) -> 30.5% (FY26)',
 'Mix + offshoring (~20%) support GM; rising DC mix pressures it',
 'Mgmt guides gross margin ~30.5%',
 'Integrators run ~20-35% GM',
 'Held ~flat-to-slightly-up; conservative given DC-mix drag; each 100bps GM ~Rs60cr+ EBITDA',
 'Medium-High','BB pres p.22')
putrow(13,'Operating expenses (SG&A) % rev',
 '21.2% (FY27E) -> 20.5% (FY32E)',
 'Total other expenses ~21.5% (FY26)',
 'Operating leverage on higher throughput + offshoring',
 'Mgmt: fixed-cost absorption drives 10% EBITDA',
 'n/a','Modest opex leverage; the main margin lever (BB has no pricing power)',
 'Medium','BB calls; model')
putrow(14,'EBITDA margin %',
 '9.3% (FY27E) -> ~10.4% (FY32E)',
 '4.3% (FY23) -> 9.0% (FY26)',
 'Operating leverage + offshoring; DC mix a drag',
 'Mgmt targets 10% by end-FY27',
 'WESCO ~7%, Kyndryl low',
 'Reaches ~10.4% - broadly in line with mgmt 10% target, capped (thin-margin, no pricing power)',
 'Medium','BB Q1FY27 pres')
putrow(15,'Depreciation & capex',
 'Dep ~13% of prior fixed assets; capex ~1.5-1.8% of revenue',
 'Dep Rs116cr (FY26); asset-light, capex small',
 'Ind-AS 116 ROU depreciation is large part of D&A',
 'Mgmt: asset-light model',
 'n/a','Low fixed-asset intensity; capex incl. lease/intangible additions',
 'Medium-High','BB pres p.22-23')
putrow(16,'Effective tax rate',
 '12% (FY27E) rising to 20% (FY32E)',
 'Reported ~3-10% (FY25 3.3%, FY26 9.2%) - NOL-driven',
 'US/global accumulated NOLs depleting; normalises to ~18-22%',
 'Not explicitly guided',
 'Statutory rates 20-25%',
 'KEY CONSERVATIVE ADJUSTMENT: normalising tax is a real PAT headwind the market underweights (flatters current EPS)',
 'Medium','BB financials; independent judgement')
putrow(17,'Finance cost / cost of funds',
 '~12% blended on borrowings (incl leases)',
 'Finance cost Rs158cr (FY26) incl lease interest + FX',
 'FY26 cost inflated by FX; assumes normalisation',
 'n/a','n/a','Bumped to 12% to capture lease + borrowing cost (ex one-off FX)',
 'Medium','BB pres; model')
putrow(18,'EPS trajectory / shares',
 'Shares 18.0cr (eq. cap Rs36cr / Rs2); EPS grows w/ PAT & tax normalisation',
 'FY26 EPS Rs12.78 (~17.1cr wtd avg)',
 'Year-end diluted ~18.0cr post warrant conversion',
 'Preferential warrants converted (Rs417)',
 'n/a','Uses ~18.0cr diluted; PAT growth partly offset by tax normalisation',
 'Medium-High','BB pres p.22-23')

# C. Working capital, capex, balance sheet
putrow(21,'DSO (receivable days)',
 '62 (FY27E) easing to 55 (FY32E)',
 'DSO jumped to ~67 (FY26) from ~35 (FY25)',
 'Month-end-skewed billing; OEM-supply-linked invoicing',
 'Mgmt claims normalised DSO ~55-60',
 'n/a','Kept ELEVATED & only gradually normalising - FY26 spike is a red flag; high DSO consumes cash',
 'Medium','BB Q2/Q3FY26 calls')
putrow(22,'Inventory (19d), DPO (46d), contract assets/liab',
 'Inventory ~19d; DPO ~46d; contract A/L scale with revenue',
 'FY26: inv ~19d, payables ~46d (on revenue); contract assets Rs280cr, liab Rs576cr',
 'Wind River licence pre-buy lifted inventory',
 'Mgmt: efficient WC',
 'n/a','Growth consumes ~0.2-0.3x revenue in WC - the structural cash constraint',
 'Medium','BB pres p.23; calls')
putrow(23,'Capex',
 '~1.5-1.8% of revenue (~Rs140-220cr/yr)',
 'Pure capex small (~Rs40-60cr); asset-light',
 'People + WC model, not capex-heavy',
 'Mgmt: asset-light',
 'n/a','Low capex supports FCF; incl. lease/intangible additions',
 'Medium','BB cash flows')
putrow(24,'Net debt / borrowings',
 'Net debt ~Rs287cr (borrowings 827 - cash 540); borrowings grow ~5-8%/yr',
 'FY26 borrowings Rs827cr + leases Rs326cr; cash Rs540cr',
 'M&A partly debt-funded; leverage target <1.5-2x',
 'Mgmt: prudent leverage',
 'n/a','Modest net debt; conservatively excludes current financial assets (Rs543cr) from cash',
 'Medium-High','BB pres p.23; independent judgement')

# D. DCF / WACC
putrow(27,'Risk-free rate','6.8%','India 10Y G-sec ~6.8-6.9% (2026)','On-the-run 10Y; INR DCF','RBI easing bias','Sovereign benchmark','Current, market-based','High','ET bond market - 2026')
putrow(28,'Equity risk premium','7.0%','India ERP ~6-7.5%','Mid-range India ERP','n/a','Standard India','7.0% (vs auto template 6.5%) reflects BB higher risk','Medium','Damodaran 2025/26')
putrow(29,'Beta (incl. size/specific risk)','1.30','Small-cap, thin-float, cyclical, ~2x move in 1yr','Sub-scale integrator + governance/concentration','n/a','Auto ~0.95; BB riskier','1.30 embeds size/specific-risk premium - defensible for a promoter-controlled small-cap','Medium','Independent judgement')
putrow(30,'WACC','~15.1%','Ke ~15.9%; after-tax Kd ~10%; weights 92/8','Materially above auto 12.7% due to higher risk','n/a','India small-cap DCFs 14-17%','Higher WACC is the disciplined choice - directly lowers DCF value','High','DCF sheet (calculated)')
putrow(31,'Terminal growth','6.0%','~4% US nominal + INR depreciation','Below India nominal GDP; mature global integrator','n/a','Mature-franchise terminal','6% INR nominal; with 15% WACC, TV multiple reasonable','Medium','Independent judgement')
putrow(32,'DCF value / share','See DCF!C41','FCFF FY27E-FY32E + TV','Conservative anchor; well below current price','n/a','Reflects 15.1% WACC / 6% g','The disciplined floor (40% blend weight)','Medium','DCF sheet')

# E. Relative
putrow(35,'Peer set',
 'WESCO, Insight, Kyndryl, Redington, HCLTech, Allied Digital',
 'BB trades ~65-70x P/E; peers ~13-22x',
 'True ECONOMIC peers (infra integrators/distributors/managed svcs) - not random IT',
 'n/a','WESCO closest analog (DC deploy + distribution)',
 'Deliberately chosen on business economics, not sector label; peer median P/E ~17-18x',
 'Medium-High','Yahoo/company filings - Aug-2026 (approx; refresh)')
putrow(36,'FY27E EPS (relative base)',
 '= Forecast!D49',
 'FY26 EPS ~Rs12.78',
 'Consol PAT / 18.0cr shares (incl tax normalisation)',
 'n/a','Drives target-price application',
 'Most sensitive to organic growth, margin & tax assumptions',
 'Medium','Model Forecast/Relative')
putrow(37,'Target P/E multiple',
 'Bear 18x / Base 25x / Bull 32x on FY27E EPS',
 'Peer median ~17-18x; BB trades ~65-70x',
 'Premium to peers for growth/DC exposure',
 'n/a','WESCO 22x; Redington 16x; HCLT 19x',
 'A GROWTH PREMIUM to peers but a large DISCOUNT to BBs current ~65-70x (partial mean-reversion)',
 'Medium','Peer multiples - 2026')
putrow(38,'EV/EBITDA (cross-check)',
 '15x FY27E EBITDA',
 'BB ~25-27x EV/EBITDA currently',
 'Third method; net debt Rs287cr',
 'n/a','WESCO ~13x; Kyndryl ~5.5x','Sanity check on P/E method; de-emphasised (20% weight)','Medium','Relative/Summary sheets')

# F. Blend & recommendation
putrow(41,'EV/EBITDA method',
 'See Summary!B10','FY27E EBITDA x 15 - net debt / shares','n/a','n/a','n/a','Corroborates relative & DCF','Medium','Summary sheet')
putrow(42,'Blend weights',
 'DCF 40% / Relative 40% / EV-EBITDA 20%','n/a','Balanced across intrinsic + market methods','n/a','n/a','DCF given high weight as the disciplined floor','Medium','Summary sheet')
putrow(43,'Blended target & recommendation',
 'See Summary!B16 (target) & B19 (reco)','Current ~Rs830','DCF + Relative + EV/EBITDA','Mgmt execution strong but plan behind schedule','Street thin/bullish','Reco is model-derived; stance cautious given valuation',
 'Medium','Cover/Summary sheets')
putrow(44,'Key limitation - historical data',
 'Full 3-statements FY21-FY26 only','BB comparable form from FY20','Pre-FY21 not comparable (AGC era)','n/a','n/a','Stated explicitly - no data invented for FY17-20','High','Phase 1 audit note')
putrow(45,'Key limitation - peer multiples',
 'Approximate, ~Aug-2026','Refresh with live data','Mixed-currency ratios (unitless)','n/a','n/a','Flagged for verification before committee use','Medium','Refresh required')

wb.save('Black_Box_Co_Model.xlsx')
print('Cover + Assumptions rebuilt & saved.')
