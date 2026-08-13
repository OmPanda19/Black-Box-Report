# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x1F, 0x38, 0x64)
GREY = RGBColor(0x40, 0x40, 0x40)

doc = Document()
# Base style
st = doc.styles['Normal']
st.font.name = 'Calibri'; st.font.size = Pt(11)
st.paragraph_format.space_after = Pt(3); st.paragraph_format.space_before = Pt(0)
st.paragraph_format.line_spacing = 1.0
for section in doc.sections:
    section.top_margin = Inches(1); section.bottom_margin = Inches(1)
    section.left_margin = Inches(1); section.right_margin = Inches(1)

def shade(cell, hexc):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:fill'),hexc)
    tcPr.append(sh)

def para(text, size=11, bold=False, color=None, after=4, before=0, italic=False, align=None):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.space_before = Pt(before); p.paragraph_format.line_spacing = 1.0
    if align: p.alignment = align
    r = p.add_run(text); r.font.size = Pt(size); r.bold = bold; r.italic = italic
    r.font.name = 'Calibri'
    if color: r.font.color.rgb = color
    return p

def heading(text):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(text); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAVY; r.font.name='Calibri'
    return p

def rich(parts, after=4):
    """parts: list of (text, bold)"""
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after); p.paragraph_format.line_spacing=1.0
    for text, bold in parts:
        r = p.add_run(text); r.bold = bold; r.font.size = Pt(11); r.font.name='Calibri'
    return p

# ---------------- TITLE ----------------
p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
r = p.add_run('Black Box Ltd (BBOX IN) — Initiation of Coverage'); r.bold=True; r.font.size=Pt(15); r.font.color.rgb=NAVY; r.font.name='Calibri'
p = doc.add_paragraph(); p.paragraph_format.space_after=Pt(6)
r = p.add_run('Digital Infrastructure / Enterprise Networking & Systems Integration  |  Buy-side investment memorandum  |  13 Aug 2026')
r.font.size=Pt(9); r.italic=True; r.font.color.rgb=GREY; r.font.name='Calibri'

# ---------------- 1. RECOMMENDATION ----------------
heading('1.  Investment Recommendation')
tbl = doc.add_table(rows=0, cols=4); tbl.style='Table Grid'; tbl.alignment=WD_TABLE_ALIGNMENT.LEFT
rows = [
 ('Recommendation','AVOID (own the watch-list, not the stock)','Current price','INR 830'),
 ('Fair value (blended)','~INR 500','Downside','~40%'),
 ('DCF / Relative / EV-EBITDA','INR 551 / 474 / 458','Horizon','12-24 months'),
]
for a,b,c,d in rows:
    cells = tbl.add_row().cells
    for i,(txt,bold) in enumerate([(a,True),(b,False),(c,True),(d,False)]):
        cells[i].text=''; rr=cells[i].paragraphs[0].add_run(txt); rr.bold=bold; rr.font.size=Pt(10); rr.font.name='Calibri'
        cells[i].paragraphs[0].paragraph_format.space_after=Pt(1)
        if bold: shade(cells[i],'EAEEF5')
for row in tbl.rows:
    for c in row.cells:
        c.width = Inches(1.6)
rich([('One-line thesis:  ', True),
 ('A genuinely repaired, blue-chip-anchored infrastructure integrator riding the AI/data-centre capex wave — but priced at ~45x FY27E earnings against ~9% EBITDA-margin, no-pricing-power, weak-cash-conversion economics and a ~26x economic-peer multiple, so the current price discounts near-flawless execution with no margin of safety.', False)], after=5)

# ---------------- 2. THESIS ----------------
heading('2.  Investment Thesis')
rich([('What the market believes.  ', True),
 ('BBOX is treated as a de-risked Indian proxy for the AI/data-centre build-out, capable of compounding to a US$2bn revenue ambition by FY30. The market extrapolates the FY23–26 margin doubling (EBITDA 4.3% → 9.0%) and the backlog surge (US$470mn → US$949mn) into a premium growth multiple, and reads the "Mag-7" hyperscaler wins as evidence of a durable, high-return franchise.', False)])
rich([('What my research concludes.  ', True),
 ('The turnaround is real, but the business is a labour-and-cabling deployment contractor, not an AI beneficiary in the way the multiple implies. It sells fibre, cabling, networking and deployment — not compute — and management concedes hyperscaler work is won on technical/safety merit, "financial parameters almost the same for everybody" (Q3 FY26): i.e., no pricing power. Revenue was flat at ~INR 6,000cr for four years (FY22 5,370 → FY26 6,322), so organic growth is unproven over a cycle, and FY26 showed backlog converts slowly and is hostage to third-party fibre/GPU/power supply. Reported profit is flattered by a ~9% NOL-shielded tax rate and 7+ quarters of "exceptional" charges. The US$2bn/FY30 target already slipped from FY29 and leans on ~INR 6,000cr of unproven serial M&A.', False)])
rich([('Why this is a limited opportunity.  ', True),
 ('The mispricing sits in the multiple, not the business, and closes through de-rating rather than deterioration. Downside to fair value is ~40%; the upside case requires out-executing repeatedly-missed guidance. For a value mandate there is no asymmetry to underwrite today.', False)])

# ---------------- 3. BUSINESS QUALITY ----------------
heading('3.  Business Quality')
rich([('Why it earns money — and the one genuine asset:  ', True),
 ('the customer franchise. 120+ Fortune-500 clients, top-10 ≈ 51% of revenue with >20-year tenures, Bank of America the largest. On mission-critical estates (banks, airports, hospitals) switching costs and downtime risk are real, underwriting a revenue floor and a recurring/managed-services base (>30% of revenue). This is what a turnaround buyer paid ~US$17mn for in 2019.', False)])
rich([('The economics that cap value:  ', True),
 ('~30.5% gross margin with heavy hardware pass-through, ~9% EBITDA on a ~INR 310–320cr/quarter fixed-cost base (operating leverage cuts both ways), and no pricing power. Asset-light but working-capital-heavy — growth consumes ~0.2–0.3x of incremental revenue. Concentration is high (top-10 51%, North America 69%) and project revenue is re-bid. A solid mid-tier integrator, not a moat business.', False)])

# ---------------- 4. FINANCIALS ----------------
heading('4.  Financial Analysis')
rich([('Growth is not yet proven.  ', True),
 ('Revenue went INR 6,282cr (FY24) → 5,967cr (FY25) → 6,322cr (FY26) — deliberate pruning of low-value accounts plus slow conversion. ', False),
 ('Margins are the real achievement:  ', True),
 ('EBITDA 4.3% (FY23) → 9.0% (FY26), driven by cost restructuring, offshoring (~20% of delivery) and mix — largely structural. ', False),
 ('Cash conversion is the tell:  ', True),
 ('operating cash flow was –INR 88cr (FY25) then +INR 84cr (FY26), and receivables spiked to INR 1,153cr (DSO ~67 days vs ~35 in FY25). ', False),
 ('Returns flatter to deceive:  ', True),
 ('ROCE in the low-30s% and PAT +49% in FY25 (to INR 205cr) reflect an asset-light, WC-financed model and a low tax rate, not a widening moat; ROE fell to ~21% in FY26 after the INR 386cr promoter-linked preferential raise. The balance sheet is fine (net debt ~INR 287cr).', False)])

# ---------------- 5. VALUATION ----------------
heading('5.  Valuation')
rich([('DCF (intrinsic anchor).  ', True),
 ('WACC 13.9% (Rf 6.8%, ERP 7.0%, beta 1.10 for a small-cap, promoter-controlled, cyclical name), terminal growth 5%, mid-year → ~INR 551. Even the most generous corner tested (12% WACC / 6% g) yields ~INR 807, and terminal value is ~67% of EV — value depends on assumptions, not the current run-rate.', False)])
rich([('Relative.  ', True),
 ('On a peer set chosen by economics — WESCO, Kyndryl, Redington (integration/distribution) and Tata Communications, Mastek, Happiest Minds (Indian tech/infra) — the median is ~26x P/E and ~9x EV/EBITDA; BBOX trades ~45x FY27E and ~65x trailing. A base 26x on FY27E EPS (~INR 18) gives ~INR 474. BBOX’s 9% EBITDA margin sits well below the software peers’ 18–22% and its growth is partly M&A/tax-driven, so it warrants a discount to high-quality IT services, not a 70–90% premium.', False)])
rich([('Blend & margin of safety.  ', True),
 ('DCF 40% / Relative 40% / EV-EBITDA (12x) 20% → ~INR 500, ~40% downside; margin of safety: none. The assumptions that matter most are organic revenue growth, sustainable EBITDA margin, the tax-normalisation path (to ~25%), and the exit multiple.', False)])

# ---------------- 6. RISKS ----------------
heading('6.  Risks (ranked; these largely support the thesis)')
rt = doc.add_table(rows=1, cols=4); rt.style='Table Grid'
hdr = ['Risk','Likelihood','Impact','Monitor']
for i,h in enumerate(hdr):
    c=rt.rows[0].cells[i]; c.text=''; rr=c.paragraphs[0].add_run(h); rr.bold=True; rr.font.size=Pt(9.5); rr.font.name='Calibri'
    shade(c,'1F3864'); rr.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
risks = [
 ('Valuation de-rating','High','High','Fwd P/E vs peers (~26x)'),
 ('Growth / guidance delivery','Med-High','High','Bookings run-rate (>US$350mn/qtr)'),
 ('Working capital / FCF','Med-High','Medium','DSO; CFO/PAT'),
 ('Governance / promoter (Essar-Ruia ~70%)','Medium','High','RPTs; issuance terms'),
 ('Customer concentration','Low-Med','High','Top-10 & BoA share'),
 ('Tax normalisation','High','Medium','Effective tax vs 25%'),
]
for a,b,c,d in risks:
    cells = rt.add_row().cells
    for i,txt in enumerate([a,b,c,d]):
        cells[i].text=''; rr=cells[i].paragraphs[0].add_run(txt); rr.font.size=Pt(9.5); rr.font.name='Calibri'
        cells[i].paragraphs[0].paragraph_format.space_after=Pt(1)
        if i==0: rr.bold=True
widths=[Inches(2.4),Inches(1.0),Inches(1.0),Inches(2.1)]
for row in rt.rows:
    for i,c in enumerate(row.cells): c.width=widths[i]

# ---------------- 7. CATALYSTS ----------------
heading('7.  Key Catalysts (value-changing, both directions)')
rich([('Negative / thesis-confirming:  ', True),
 ('another guidance cut; AI-capex digestion; a working-capital blow-out or dilutive raise. ', False),
 ('Positive / thesis-invalidating:  ', True),
 ('sustained bookings >US$350mn/quarter with repeatable hyperscaler data-centre wins carrying annuity tails; EBITDA crossing ~10.5% with exceptionals ending; the first clean FCF-positive year (CFO/PAT >0.8); an accretive 2S-style acquisition; and the first meaningful mutual-fund entry (a re-rating validator).', False)])

# ---------------- 8. CONCLUSION ----------------
heading('8.  Conclusion')
rich([('The market believes ', False),
 ('Black Box is a de-risked Indian proxy for the AI/data-centre build-out that will compound to a US$2bn revenue base and premium returns', True),
 (', whereas my research indicates ', False),
 ('a much-improved but thin-margin, cash-light, no-pricing-power integrator whose organic growth is unproven over a cycle and whose earnings are flattered by a temporary tax rate and recurring "exceptionals"', True),
 (', because ', False),
 ('four years of flat organic revenue, negative-to-volatile free cash flow, a slipped FY30 target, ~0% mutual-fund ownership and a ~26x economic-peer multiple do not support ~45x forward earnings.', True)])
rich([('Do not own the stock at INR 830. ', True),
 ('The business is worth tracking; the equity is not worth buying here. Re-underwrite on two-plus quarters of >US$350mn bookings with visible data-centre annuity conversion, EBITDA >10.5% and positive free cash flow; a constructive entry aligns with fair value (~INR 480–520), with a real margin of safety below that. All facts trace to the FY24–25 Annual Report, FY26 presentations, Q1–Q3 FY26 calls and the accompanying model; peer multiples (~Aug-2026) to be refreshed before committee.', False)])

doc.save('Black_Box_Investment_Memo.docx')
print('Memo saved.')
