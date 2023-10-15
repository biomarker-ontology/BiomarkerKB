# v2.0 Release Notes 

## Data changes 
- The `main_x_ref` column has been renamed to `assessed_biomarker_entity_ID`.
- The `biomarker_status` column has been renamed to `biomarker`.
- The `specimen_type` column has been split into `specimen_ID` and `specimen` columns to increase parsability.
- The `condition_name` column has been split into `condition_ID` and `condition` columns to increase parsability.
- The following columns have been added[^1]:
    - `exposure_agent_ID`
    - `exposure_agent` 
- The `evidence_source` column has been split into `evidence_source`[^2] and `evidence`[^3] columns to increase parsability.
- Column ordering updated to:
    - biomarker_ID 
    - biomarker 
    - assessed_biomarker_entity
    - assessed_biomarker_entity_ID 
    - assessed_entity_type
    - best_biomarker_type 
    - condition 
    - condition_ID 
    - exposure_agent 
    - exposure_agent_ID 
    - specimen 
    - specimen_ID 
    - loinc_code
    - evidence_source 
    - evidence 
    - notes 

## Schema Changes:
- "biomarker_ID" set to optional, it will be assigned when the data is incorporated.
- "condition" and "condition_ID" are conditionally required based on the presence of one of the values.
- "exposure_agent" and "exposure_agent_ID" are conditionally required based on the presence of one of the values.
- The pairs of ("condition", "condition_ID") and ("exposure_agent", "exposure_agent_ID") are mutually exclusive, a given record will have either condition or exposure data.
- "specimen" set to optional.
- "specimen_ID" set to optional.
- "loinc_code" set to optional.
- "evidence" set to optional. 

## Structure Changes
- Added ability to add conditional and exclusive requirements.
    - Conditionals: Properties that are conditionally required based on the presence of other properties. 
        - Example: In the row for the "condition" property, the property "condition_ID" is set as a conditional requirement. If the "condition" property is included, then the "condition_ID" property is required (and vice versa).
    - Exclusions: Properties that are mutually exclusive based on the presence of other properties.
        - Example: In the row for the "condition" property, the properties "exposure_agent" and "exposure_agent_ID" are set as exclusion requirements. If the "condition" property is included, then the "exposure_agent" and "exposure_agent_ID" are not to be included. 
  
## Footnotes
  
[^1]: A given record will have either condition information or expsure_agent information.  
[^2]: The evidence_source column will optimally be formatted as Resource:Identifier (e.x. PMID:12345).  
[^3]: The evidence column would be "some text sentence" and would be populated by manual curation or natural langauge processing (NLP).