# Radiation and water on Pine Ridge

An executed educational notebook using historical published USGS measurements.

## Open

- `pine_ridge_radiation.html`: read the lesson and figures in a browser.
- `pine_ridge_radiation.ipynb`: open in Jupyter or upload to Google Colab. Run cells in order. The notebook contains an embedded, checksum-verified data snapshot and can run without the companion files or network access once dependencies are installed.

For a local environment with Python 3.11 or later:

```sh
python -m pip install -r requirements.txt
python -m jupyter lab pine_ridge_radiation.ipynb
```

## Contents

- `data/historical_results.csv`: 540 selected analyte slots, of which 240 contain results or less-than bounds. Covers 44 public-supply well sites and 14 spring sites. Missing cells remain explicit.
- `data/provenance.json`: source URL, PDF and CSV checksums, extraction details, and known issues.
- `sources/wri994063.pdf`: original USGS report, including methods, tables and footnotes.
- `sources/pdf_page_*.txt`: extracted page text used for the snapshot and metadata.
- `radiation_results/`: interpreted table, coverage summary, five PNG figures, and tested environment metadata.
- `source_inventory.md`: broader source leads and initial scope.
- `reextract.py`: regenerate the selected CSV from the supplied PDF. Requires `pdfplumber` in addition to the analysis dependencies; run from any directory with `python /path/to/reextract.py`. It overwrites the derived CSV and provenance in this folder. The notebook checksum should match the regenerated snapshot; investigate any mismatch rather than bypassing the check.

## Source and checks

Heakin, A.J. (2000), *Water quality of selected springs and public-supply wells, Pine Ridge Indian Reservation, South Dakota, 1992-97*. USGS WRI 99-4063, prepared in cooperation with the Oglala Sioux Tribe. https://doi.org/10.3133/wri994063

The extraction selects dissolved natural uranium, gross alpha as Th-230, gross beta as Cs-137, and radium-226 from Tables 13 and 14. Printed pages 51–52 and 59–61 correspond to PDF pages 56–57 and 64–66. Well metadata and treatment-stage context come from printed pages 12–13.

Verification includes strict extraction column counts, site and row counts, unique keys, preservation of less-than bounds and missing cells, visual inspection of source pages, a 44-value uranium comparison, and agreement with historical report summary counts. All 11 notebook code cells were executed successfully in a fresh Jupyter kernel; figures were visually reviewed.

Two source-date discrepancies remain explicitly unresolved: site 27 on the uranium page, and site 42 between Table 3 and Table 14. Both sites are excluded from the date-based well summary while their printed values remain in value-only plots. Springs' gross-beta uncertainties occur on the next source page; the CSV includes the separate uncertainty page reference.

## Interpretation

This lesson describes historical selected samples. It distinguishes upstream and downstream treatment sampling, mass and activity concentration, analytical uncertainty, and measurement gaps. It does not infer mining attribution, convert gross beta to dose, or substitute simulated observations.

EPA reference checked October 27, 2026: https://www.epa.gov/dwreginfo/radionuclides-rule

This is a working instructional artifact for the NIFA series. It makes no claim of OLC/OST endorsement, approved release status, or confirmed award attribution. No new household records or precise-coordinate map is included.
