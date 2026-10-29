from pathlib import Path
import re, csv, json, hashlib, shutil
import pdfplumber

root = Path(__file__).resolve().parent
(root/'data').mkdir(parents=True, exist_ok=True)
(root/'sources').mkdir(exist_ok=True)
pdf_path = root/'sources/wri994063.pdf'
pdf = pdfplumber.open(pdf_path)
texts = [p.extract_text() for p in pdf.pages]
url = 'https://pubs.usgs.gov/wri/wri994063/wri994063.pdf'

def well_rows(page, width):
    rows = {}
    for line in texts[page-1].splitlines():
        t = line.split()
        if len(t) >= 2 and re.fullmatch(r'\d{1,2}',t[0]) and re.fullmatch(r'\d{2}-\d{2}-\d{2}',t[1]):
            assert len(t) == width+2, (page,line,t)
            rows[int(t[0])] = (t[1],t[2:])
    assert set(rows) == set(range(1,45)), (page,len(rows))
    return rows

w_alpha = well_rows(64,9)
w_beta = well_rows(65,8)
w_u = well_rows(66,6)
metadata = {}
for line in texts[16].splitlines():
    t=line.split()
    if len(t)>3 and re.fullmatch(r'\d{1,2}',t[0]) and re.fullmatch(r'\d{15}',t[1]):
        date = next(x for x in t if re.fullmatch(r'\d{2}-\d{2}-\d{2}',x))
        aquifer = 'Inyan Kara' if 'Kara' in t else t[-1]
        metadata[int(t[0])] = dict(site_id=t[0], station_id=t[1], aquifer=aquifer,
            site_table_date=date, treatment_stage='downstream of treatment' if int(t[0]) in (6,11,12) else 'upstream of treatment')
assert len(metadata)==44

def spring_rows(page,width):
    rows = {}; site = None
    for line in texts[page-1].splitlines():
        t=line.split()
        if t and re.fullmatch(r'S\d{1,2}',t[0]): site=t.pop(0)
        if t and re.fullmatch(r'\d{2}-\d{2}-\d{2}',t[0]):
            assert site is not None and len(t)==width+1,(page,line)
            key = (site,t[0]); assert key not in rows
            rows[key] = t[1:]
    assert len(set(s for s,d in rows))==14
    return rows
s_alpha = spring_rows(56,9)
s_u = spring_rows(57,7)
assert s_alpha.keys()==s_u.keys()

def parsed(raw):
    if raw=='--': return dict(result_numeric='',qualifier='not_reported',reporting_bound='')
    if raw.startswith('<'): return dict(result_numeric='',qualifier='less_than',reporting_bound=float(raw[1:]))
    return dict(result_numeric=float(raw),qualifier='reported_numeric',reporting_bound='')

data=[]
def add(site,kind,date,analyte,raw,unc,code,page,meta=None):
    meta = meta or {}
    row=dict(source_id='USGS_WRI_99_4063',source_url=url,source_table=14 if kind=='well' else 13,
        source_pdf_page=page,source_printed_page=page-5,
        uncertainty_source_pdf_page=57 if kind=='spring' and analyte=='gross_beta' else page,
        site_id=site,site_type=kind,
        sample_date_original=date,analyte=analyte,parameter_code=code,
        result_original=raw,unit='ug/L' if analyte=='uranium' else 'pCi/L',
        uncertainty_2sigma_original=unc,measured_or_estimated='reported laboratory result' if raw!='--' else 'not reported',
        date_note='Site 27: page 61 prints 01-29-95; other Table 14 pages and Table 3 print 11-29-95; left unresolved.' if site=='27' and kind=='well' else '',
        treatment_stage=meta.get('treatment_stage','not established'),aquifer=meta.get('aquifer','not extracted'),
        station_id=meta.get('station_id',''),site_table_date=meta.get('site_table_date',''),
        analytical_description={'uranium':'Dissolved natural uranium, as U',
          'gross_alpha':'Dissolved gross alpha radioactivity, as Th-230',
          'gross_beta':'Dissolved gross beta radioactivity, as Cs-137',
          'radium_226':'Dissolved radium-226, planchet count'}[analyte])
    row.update(parsed(raw)); data.append(row)

for site in range(1,45):
    m=metadata[site]; ds,va=w_alpha[site]; db,vb=w_beta[site]; du,vu=w_u[site]
    assert ds==db
    add(str(site),'well',ds,'gross_alpha',va[5],va[6],'04126',64,m)
    add(str(site),'well',db,'gross_beta',vb[0],vb[1],'03515',65,m)
    add(str(site),'well',db,'radium_226',vb[4],vb[5],'09510',65,m)
    add(str(site),'well',du,'uranium',vu[4],vu[5],'22703',66,m)

for (site,date),va in s_alpha.items():
    vb=s_u[(site,date)]
    add(site,'spring',date,'gross_alpha',va[4],va[5],'04126',56)
    add(site,'spring',date,'gross_beta',va[8],vb[0],'03515',56)
    add(site,'spring',date,'radium_226',vb[3],vb[4],'09510',57)
    add(site,'spring',date,'uranium',vb[5],vb[6],'22703',57)

with (root/'data/historical_results.csv').open('w',newline='',encoding='utf-8') as f:
    wr=csv.DictWriter(f,fieldnames=list(data[0])); wr.writeheader(); wr.writerows(data)

# Retain source evidence, including table headings and the study sampling methods.
for page in [17,18,56,57,58,64,65,66]:
    (root/f'sources/pdf_page_{page:02}.txt').write_text(texts[page-1],encoding='utf-8')
# Original source PDF already resides in sources/.
manifest=dict(source_url=url,doi='10.3133/wri994063',retrieved='2026-10-27',
    pdf_sha256=hashlib.sha256(pdf_path.read_bytes()).hexdigest(),
    csv_sha256=hashlib.sha256((root/'data/historical_results.csv').read_bytes()).hexdigest(),
    result_rows=len(data),well_sites=44,spring_sites=14,spring_sample_rows=len(s_u),
    extraction='PDF text extraction with column-count assertions; result and qualifier strings retained.',
    known_issues=['Site 27 uranium page date differs from other pages; no correction applied.',
                  'Site 42 Table 3 date differs from Table 14; analytical pages retained.',
                  'Gross beta uncertainty is on the following source page for springs.'])
(root/'data/provenance.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(manifest,indent=2))
