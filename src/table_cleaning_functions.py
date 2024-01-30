''' Helper functions that can be imported in other scripts to clean table formatted data.
'''

import pandas as pd 
import re 
import json

TSV_HEADERS = ['biomarker_id', 'biomarker', 'assessed_biomarker_entity', 'assessed_biomarker_entity_id', 
            'assessed_entity_type', 'condition', 'condition_id', 'exposure_agent', 'exposure_agent_id', 
            'best_biomarker_role', 'specimen', 'specimen_id', 'loinc_code', 'evidence_source', 'evidence',
            'tag']

PREFIX_MAP_PATH = '../mapping_data/prefix_map.json'
with open(PREFIX_MAP_PATH) as f:
    PREFIX_MAP = json.load(f)

def map_prefixes(source_column: pd.Series) -> pd.Series:
    ''' Maps the prefixes in the given dataframe column.

    Parameters
    ----------
    source_column: pd.Series
        The dataframe column to clean.
    
    Returns
    -------
    pd.Series
        The cleaned dataframe column.
    '''
    return source_column.apply(lambda x: x.replace(x.split(':')[0], PREFIX_MAP[x.split(':')[0].lower()]).strip() if pd.notnull(x) and x.split(':')[0].lower() in PREFIX_MAP else x)

def clean_parantheticals(source_column: pd.Series) -> pd.Series:
    ''' Cleans the parantheticals in the given dataframe column.

    Parameters
    ----------
    source_column: pd.Series
        The dataframe column to clean.
    
    Returns
    -------
    pd.Series
        The cleaned dataframe column.
    '''
    return source_column.apply(lambda x : x.split('(')[0].strip() if isinstance(x, str) else x)

def strip_values(source_column: pd.Series) -> pd.Series:
    ''' Strips the leading and trailing whitespace from the given dataframe column.

    Parameters
    ----------
    source_column: pd.Series
        The dataframe column to clean.
    
    Returns
    -------
    pd.Series
        The cleaned dataframe column.
    '''
    return source_column.apply(lambda x: x.strip() if isinstance(x, str) else x)