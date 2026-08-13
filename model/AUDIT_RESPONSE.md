# Response to Due-Diligence Audit — Black Box Model

This documents how each audit recommendation was handled. Every valid methodological point was implemented; factually incorrect "corrections" were rejected **with evidence** (per the instruction to cross-check against official financials and to avoid introducing inconsistencies).

## CRITICAL: the audit's "historical corrections" were based on a fiscal-year mix-up — REJECTED
The audit claimed FY25 consolidated **PAT ₹137.67cr / PBT ₹156.39cr**, borrowings **₹397cr ("down from ₹654cr")**, and contract assets/liab **₹246cr/₹501cr**. These are **FY24 (year-ended Mar-2024) figures mislabelled as FY25.**

The **audited FY24-25 Annual Report — Directors' Report/MD&A (p.94-95)** states verbatim for FY2025 (consolidated):
- Revenue ₹5,967cr (−5% vs ₹6,282cr FY24)
- EBITDA ₹531cr, margin 8.9% (vs 6.8% FY24)
- **PBT ₹212cr (from ₹156cr)**
- **PAT ₹205cr (from ₹138cr), +49%**
- Total equity ₹759cr (from ₹481cr); Finance costs ₹145cr; Depreciation ₹113cr

The model already matched these audited values exactly. Adopting the audit's numbers would have **replaced correct FY25 figures with FY24 figures** — so they were rejected. Likewise, FY25 borrowings **rose** to ₹654cr (not "down to ₹397cr"): ₹397cr was FY24. A reconciliation note is on the Assumptions sheet (row 44).

| Audit "FY25" claim | Actually is | Correct FY25 (audited) | Model |
|---|---|---|---|
| PAT ₹137.67cr | FY24 PAT (₹138cr) | **₹205cr** | ₹205 ✓ |
| PBT ₹156.39cr | FY24 PBT (₹156cr) | **₹212cr** | ₹212 ✓ |
| Borrowings ₹397cr | FY24 (₹362+35) | **₹654cr** (₹633+21) | ₹654 ✓ |
| Contract A/L ₹246/₹501cr | FY24 (Mar-24) | ₹219 / ₹500cr | matches ✓ |

## Valid recommendations — IMPLEMENTED
| # | Recommendation | Action taken |
|---|---|---|
| 2 | Remove residual TVS metrics | Already done in prior build (0 auto references; revenue driven by organic/inorganic growth, DSO, cost-of-revenue). Re-verified. |
| 3 | Surface contract assets/liabilities | Added explicit **Section 7 — Contract Accounting** on Operating Drivers (contract assets & liabilities in ₹cr, FY21-FY26); already flow through forecast working capital as % of revenue. |
| 4 | Normalise tax to statutory | Tax rate glide changed to **12% → 25%** (FY27E→FY32E) as US/India NOLs deplete (was 12%→20%). Terminal now at statutory 25%. |
| 6 | WACC & terminal growth | **Beta 1.30 → 1.10**; Ke 14.5%; **WACC 15.2% → 13.9%** (toward the audit's 11-13%). **Terminal g 6% → 5%**. **Mid-year convention** added to discounting (best practice). Sensitivity table recentred to **WACC 12-15% × g 3-6%** and made mid-year. |
| 6 | Capex realism | Capex reduced/reclassified to ~1.1-1.3% and **relabelled** to clarify it includes ROU/lease + intangible additions (pure cash capex ~0.7-1.0% per FY25); depreciation 12.5% keeps the fixed-asset roll-forward consistent (Ind-AS 116 ROU amortisation). |
| 7 | Peer group | Expanded to span **global economic analogs (WESCO, Kyndryl, Redington)** + **Indian listed tech/infra (Tata Communications, Mastek, Happiest Minds)**. Peer median P/E ~26x, EV/EBITDA ~9x. EV/EBITDA cross-check target aligned to 12x. |
| 8 | Formula/link audit | Re-verified: 0 #REF/#DIV/#VALUE, no circular references, balance sheet balances every year, cash flow reconciles, mid-year sensitivity grid recomputes dynamically. |

## Recommendations reviewed but not adopted (with reasoning)
- **Revenue growth 8-10%** (audit): retained **organic 13%→9%** because the US$949mn backlog (Q1FY27) and management's +23-27% FY27 guidance support higher near-term growth; my path is still below management and layered with (challenged) M&A.
- **DSO ~24 days / "25% of revenue"** (audit, from FY25's low ₹386cr receivables): retained **DSO 62→55** because FY26 receivables spiked to ₹1,153cr (~67 days); the audit's own alternative ("stabilise at 60-70 DSO") matches the model.
- **Flat 25% tax from FY27**: used a **glide** instead — the US NOLs genuinely shield near-term tax (FY26 effective ~9%); jumping to 25% immediately would contradict FY27 PAT reality and management's ₹300-325cr guidance. Terminal rate is 25%.

## Net effect on valuation
| Method | Before audit response | After |
|---|---|---|
| DCF (WACC / g) | ₹467 (15.2% / 6%) | **₹551** (13.9% / 5%, mid-year) |
| Relative (base) | ₹469 (26x) | **₹474** (26x; refreshed peers) |
| EV/EBITDA | ₹497 (13x) | **₹458** (12x) |
| **Blended target** | ₹474 | **₹502** |
| Upside vs ₹830 | −43% | **−40%** |
| Recommendation | Reduce | **Reduce** |

The moderated (more defensible) WACC and mid-year convention lifted the DCF; higher terminal tax and lower terminal growth partly offset. The conclusion is unchanged and now rests on **more institutionally-standard inputs**: at ~45x FY27E EPS (vs a refreshed economic-peer median ~26x) Black Box remains priced well above fundamental fair value — a genuinely improved business whose equity is priced for perfection.
