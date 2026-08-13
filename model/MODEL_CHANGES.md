# Black Box Ltd — Financial Model (converted from TVS Motor template)

**File:** `Black_Box_Co_Model.xlsx` · **Structure preserved** (8 sheets, same layout, formatting, colour coding) · **Only automotive-specific content replaced.**

> The workbook recalculates on open (fullCalcOnLoad=True). Open in Excel/LibreOffice to see computed values.

## What the base template was
A complete **TVS Motor** model with the titles relabelled "Black Box." Every number, formula and driver was automotive (Volume × ASP revenue, EV penetration, TVS Credit NBFC SOTP, Hero/Bajaj/Eicher peers). See `PHASE1_AUDIT_AND_MAPPING.md` for the full audit and the TVS→Black Box metric map.

## Phase-by-phase changes
- **Historicals** — repopulated with Black Box **consolidated** IS/BS/CF for **FY21–FY26** (complete) plus FY19–FY20 partial P&L. Balance sheet ties exactly (cash used as the reconciling plug, matching reported cash within rounding). P&L restructured to Black Box's reported lines (Revenue → Gross Profit → Total Other Expenses → EBITDA → … → PAT). Auto line-items relabelled (Cost of Materials → Cost of Revenue; ROU/Goodwill/contract assets & liabilities surfaced). *Limitation:* FY17–FY18 (AGC era) not comparable → left blank with a note.
- **Operating Drivers** — replaced vehicle-volume/ASP/EV-penetration with services KPIs: revenue growth (organic vs inorganic), segment mix (GSI/TPS), data-centre & recurring-services mix, geographic mix, gross/EBITDA/EBIT margins, DSO/DPO/inventory days, contract assets/liabilities % of revenue, net debt, tax, ROE. Historical columns computed from Historicals; forecast columns linked to the Forecast assumptions.
- **Forecast** — revenue rebuilt as **organic growth % + inorganic (acquired) revenue** (no units × price). Costs re-based to **cost-of-revenue % (gross margin)** and **SG&A %**; tax rate **normalised 12%→20%** (NOL depletion); effective finance cost captures lease interest; **exceptional items** tapered in (mgmt flagged continuation); EPS on **18.0cr shares**. 3 statements fully articulated; balance check and cash tie = 0 in every year.
- **DCF** — WACC rebuilt for a small-cap integrator: Rf 6.8%, ERP 7.0%, **beta 1.30** (size/specific-risk), Ke ~15.9%, marginal cost of debt 9%, **WACC ~15.2%**; **terminal g 6%**; **net debt ₹287cr**; shares 18.0cr. FCFF cleaned of the NBFC adjustment. Excel DataTable replaced with **explicit, self-recomputing sensitivity formulas** (WACC 13–16% × g 4–6.5%).
- **Relative** — economic peer set (**WESCO, Insight, Kyndryl, Redington, HCLTech, Allied Digital**) rather than random IT names; peer median P/E ~17.5x. Target P/E: bear 20x / base 26x / bull 32x on FY27E EPS (premium to peers for growth, deep discount to BBOX's ~46–68x). *Peer multiples are approximate (~Aug-2026) — refresh with live data.*
- **Summary** — TVS-Credit NBFC SOTP replaced with an **EV/EBITDA cross-check** (13x FY27E EBITDA) as the third method. Triangulation: **DCF 40% / Relative 40% / EV-EBITDA 20%** → blended target, upside, recommendation.
- **Cover / Assumptions** — thesis, pillars, catalysts, risks and full assumption documentation rewritten for Black Box, with historical basis, industry rationale, management commentary, independent judgement and source per assumption.

## Model output (fully formula-linked)
| Method | Value (₹/sh) |
|---|---|
| DCF (WACC 15.2%, g 6%) | ~467 |
| Relative (26x FY27E EPS, base) | ~469 |
| EV/EBITDA (13x FY27E) | ~497 |
| **Blended target** | **~474** |
| Current price | 830 |
| **Upside / (downside)** | **~ −43% → REDUCE** |

FY27E: revenue ~₹7,644cr (mgmt ₹7,800–8,000cr), EBITDA margin 9.3%→10.4% by FY32E, PAT ~₹325cr (in line with mgmt ₹300–325cr), EPS ~₹18. At ₹830 the stock trades ~46x FY27E EPS vs an economic-peer median ~17.5x.

## Interpretation (stance)
The business assumptions are fair-to-generous (13% organic growth, margin reaching ~10.4%, PAT in line with management). The downside is driven almost entirely by **valuation** — a fundamental fair value well below the market price. Even the most generous DCF corner (13% WACC, 6.5% g) is ~₹672 (−19%). This corroborates the initiation thesis: Black Box is a genuinely improved business, but the equity is **priced for perfection** with little margin of safety. Model-derived call at the current price: **Reduce / Underweight on valuation** (constructive on the business).

## QC performed
Balance sheet balances every year; cash flow reconciles; no #REF/#DIV/#VALUE; no circular references; no leftover TVS/automotive text; sensitivity grid recomputes dynamically; all cross-sheet links resolve.

## Stated limitations (no data invented)
1. Full consolidated 3-statements only FY21–FY26 (BB's comparable form dates from FY20); FY17–FY18 left blank.
2. Peer multiples are approximate as of ~Aug-2026 and should be refreshed with live data.
3. Segment/geographic mix history is only fully disclosed for FY26.
