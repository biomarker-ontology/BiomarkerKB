# v0.3.3 Release Notes

## Changes
- ID fields simplified: 
    - `specimen_id` changed to `id`
    - `biomarker_component[evidence_source][evidence_id]` changed to `id`
    - `condition_id` changed to `id`
    - `condition[synonyms][synonym_id]` changed to `id`
    - `evidence_source[evidence_id]` changed to `id`
    - `exposure_agent_id` changed to `id`
    - `citation[evidence_source][evidence_id]` changed to `id`
    - `citation[reference][reference_id]` changed to `id`
- `citation[evidence_source]` to an array.
