# Pine Ridge radiation: initial source inventory

## Recommendation

Begin with **Radiation and water on Pine Ridge: historical measurements and monitoring gaps**. The sources below support a historical evidence notebook. A later module could address indoor radon and soil or ambient radiation once relevant local measurements are located.

This is a source-level inventory. Sample coordinates, analytical methods, and reuse terms still require examination before mapping.

## Sources inspected

### 1. USGS/Oglala Sioux Tribe water-quality study (first extraction priority)

Heakin (2000), *Water quality of selected springs and public-supply wells, Pine Ridge Indian Reservation, South Dakota, 1992–97*, WRI 99-4063.

- Coverage: 14 contact springs and 44 public-supply wells; well sampling occurred during 1995–1997.
- Relevant data: uranium, gross alpha, radium, and selected uranium-isotope analyses; report tables are a candidate for structured extraction.
- Access: [publication and abstract](https://pubs.usgs.gov/publication/wri994063), [report PDF](https://pubs.usgs.gov/wri/wri994063/wri994063.pdf).
- Interpretation: the report uses historical standards, including a proposed uranium value. Preserve its original comparisons separately from comparisons with current benchmarks. Its gross-alpha results cannot automatically be labeled regulatory exceedances; the report explicitly explains the uranium/radon exclusions and analytical limitations.
- Status: publication verified; individual result rows and machine-readable equivalents not yet verified. Historical source-water observations cannot describe today's treated tap water.

### 2. Swift Bird, Navarre-Sitchler, and Singha (2020) interpretation and data-access lead

*Hydrogeological controls of arsenic and uranium dissolution into groundwater of the Pine Ridge Reservation, South Dakota*, Applied Geochemistry 114, 104522.

- Methods describe 253 domestic wells installed by IHS during 1990–2016; records were obtained through collaboration with OST and the IHS Martin field office.
- Direct uranium measurements were available for 107 wells. Other uranium values were estimated from gross alpha. These must remain explicitly distinguishable.
- Useful context: relationships between aquifer chemistry and uranium mobility.
- Access: [author-hosted paper](https://people.mines.edu/ksingha/wp-content/uploads/sites/44/2021/03/swiftbird_etal2020.pdf), [DOI](https://doi.org/10.1016/j.apgeochem.2020.104522).
- Status: methods verified; a public, reusable row-level data download was not established in this review. 
- Notebook use: discuss the published methods and findings; use underlying records only through an appropriate authorized access route.

### 3. Defenders of the Black Hills (March 2011) (community-origin source)

Charmaine White Face, *Report on Water Tests for Radioactive Contamination*.

- [Public report](https://www.defendblackhills.org/document/waterreport32011.pdf).
- Describes regional water sampling and includes a Pine Ridge/Red Shirt discussion.                                                     
- Status: report and sampling narratives inspected; original laboratory attachments, dates, units, methods, and exact geographic coverage need verification before numerical reuse.
- Notebook use: include community-origin questions and evidence alongside institutional sources. Separate reported analytical results from the report's interpretations and recommendations. Independently verify any health, regulatory, or source-attribution claim before carrying it into instructional material.

### 4. EPA Radionuclides Rule (interpretation reference)

[Official rule page](https://www.epa.gov/dwreginfo/radionuclides-rule).

The page lists uranium at 30 µg/L, combined radium-226/228 at 5 pCi/L, gross alpha at 15 pCi/L excluding radon and uranium, and beta/photon emitters at 4 mrem/year. These benchmarks concern community drinking-water systems.                                    

Mass concentration (µg/L), activity concentration (pCi/L), and dose (mrem/year) are different quantities. Do not apply a universal conversion between uranium mass and activity. Do not use an indoor-air radon benchmark to interpret water samples.

## Further searches needed

| Candidate | Question to resolve | Current status |
|---|---|---|
| USGS water-quality records/Water Quality Portal | Can historical report samples be retrieved with stable site and result identifiers? Are there newer local measurements? | Not established; portal homepage timed out during this review |
| Local public-water-system reports | Which systems actually serve the study communities, and what sampling dates and treatment stages do their records represent? | System identities and records not yet verified |
| Indoor radon measurements | Is locally relevant measured coverage available at an appropriate publication scale? | No local measurement dataset verified |
| Soil, sediment, and ambient radiation | Which records measure these media on Pine Ridge rather than elsewhere in the region? | No local dataset verified |

Geographic validation is essential: searches also return unrelated places and projects named Pine Ridge, including in Wyoming and other states.

## Proposed notebook structure

1. Frame the community question and distinguish water, indoor air, soil, and ambient radiation.
2. Introduce the historical USGS study, sampling dates, and coverage limitations.
3. Load a verified table with a citation and extraction provenance for each row.
4. Plot results by analyte and date, retaining nondetects, uncertainty, and analytical qualifiers.
5. Show monitoring coverage at an appropriate scale; distinguish unsampled, not tested for this analyte, nondetect, and detected.
6. Compare eligible results with clearly dated reference values, without assigning compliance or household safety labels.
7. Identify unanswered questions for community-directed monitoring.

Do not interpolate a continuous radiation-risk surface from sparse historical samples. Do not infer a contamination source from proximity to mining or from uranium concentration alone. Leave source attribution as a question unless supported by appropriate hydrogeological and analytical evidence.

## Minimum data schema

`source_id`, `source_url`, `source_table_page`, `original_site_id`, `sample_id`, `sample_date`, `sample_medium`, `treatment_stage`, `analyte`, `result_original`, `result_numeric`, `unit`, `qualifier`, `detection_limit`, `reporting_limit`, `uncertainty`, `method`, `measured_or_estimated`, `aquifer`, `location_precision`, `reuse_status`.

Keep nondetects separate from zero. Preserve original units and identifiers. Retain exact coordinates only where appropriate for the authorized use; the initial public teaching artifact can use aggregate coverage.

## Readiness

**Ready:** a locally relevant historical source, a later scientific study, a community-origin report, and an authoritative interpretation reference.

**Still required before a measurement notebook:** extract and verify report tables, establish result-level provenance and reuse conditions, check newer records, and confirm an appropriate geographic presentation. No simulated observations should fill missing measurements.
