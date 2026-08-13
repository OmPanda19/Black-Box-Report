# Phase 1 — Audit of Existing Model & TVS → Black Box Mapping

## Workbook structure (8 sheets, preserved)
| Sheet | Purpose | Key layout |
|---|---|---|
| Cover | Investment summary/thesis | C6 current price; links to Summary/DCF/Relative |
| Historicals | IS (r3-36), BS (r39-84), CF (r87-119) | Cols B–K = FY17–FY26 (K=FY26) |
| Operating Drivers | Volume/ASP drivers | Cols C–L = FY17–26, M–R = FY27E–32E |
| Forecast | 3-statement forecast + checks | Col C = FY26A, D–I = FY27E–FY32E |
| DCF | WACC, FCFF, TV, sensitivity | FCFF B–G = FY27E–32E |
| Relative | Peer table + target multiple | Peers r5-7; TP r19-21 |
| Summary | SOTP + triangulation + reco | Blended target B16 |
| Assumptions | Documentation grid | 6 blocks |

## Formatting conventions (preserved)
- Title bars: dark blue fill `FF002060`, white bold.
- Section headers: red bold `FFFF0000`.
- Year headers: blue bold `FF002060`.
- Inputs: blue font; formulas: black. Number formats: `#,##0` (values), `0.0%` (rates), accounting fmt (forecast), `0.00` (checks).

## Diagnosis
The workbook is a **complete TVS Motor model with only titles relabelled "Black Box."** Every number, formula and driver is automotive. It must be re-based to Black Box's actual consolidated financials and re-driven on services-integrator economics.

## TVS metric → Black Box equivalent (mapping)
| TVS (auto) metric | Black Box equivalent | Treatment |
|---|---|---|
| Vehicle volume (units) | Revenue build: organic growth % + inorganic (acquired) revenue ₹cr | REPLACE driver |
| ASP / realisation per unit | n/a (no units) — revenue = organic base × (1+g) + M&A | REPLACE |
| EV penetration / EV 2W share | Data-centre revenue mix %; managed-services/recurring % | REPLACE |
| Export mix / domestic mix | Geographic mix (NA 69%, Europe, India, APAC, LatAm, MEA) | REPLACE |
| Premiumisation (>125cc) | Segment mix: GSI ~84% / TPS ~14% / Other ~2% | REPLACE |
| Cost of materials % (~59%) | Cost of revenue % = 1 − gross margin (~69.5%) | RE-BASE |
| Employee % + Other exp % | Total operating expenses (SG&A) % of revenue (~21.5%) | RE-BASE |
| Dealer inventory / inventory days (16) | Inventory days (~19, incl. licence stock) | RE-BASE |
| Receivable days (17) | DSO (~55–67; elevated) | RE-BASE |
| Payable days (64) | DPO (~46) | RE-BASE |
| (buried) | Contract assets / contract liabilities (in other CA/CL, % of revenue) | SURFACE |
| Tax rate 25% | Effective tax rising 12%→20% (NOL depletion) | RE-BASE (key) |
| NBFC loan book / TVS Credit AUM | n/a (no captive finance) — remove NBFC lines | REMOVE |
| Minority interest growth 8% | ~0 (BB equity attributable to owners) | RE-BASE→0 |
| Auto beta 0.95, ERP 6.5%, WACC 12.7% | Beta 1.30, ERP 7.0%, WACC ~15% (small-cap/risk) | RE-BASE |
| Net cash +₹3,164cr | Net debt ≈ ₹287cr (borrowings 827 − cash 540) | RE-BASE |
| Shares 47.51cr | Shares 18.0cr (equity capital ₹36cr / ₹2) | RE-BASE |
| Peers: Hero/Bajaj/Eicher | WESCO, Insight, Kyndryl, Redington, HCLTech, Allied Digital | REPLACE |
| TVS Credit NBFC SOTP (3.5x P/B) | EV/EBITDA cross-check (no SOTP) | REPLACE |

## Historical data availability (limitation, stated explicitly)
Black Box in its current consolidated form dates from FY20 (post the Jan-2019 Black Box Corporation acquisition). **Complete consolidated 3-statements are available for FY21–FY26 (6 years)** from the FY26 investor presentation (pages 21–24) and annual reports. FY19–FY20 have only summary P&L (revenue/EBITDA/PAT); FY17–FY18 (AGC Networks micro-cap era) are not comparable and are left blank. This is the maximum reliable history the workbook can support.
