import pandas as pd 
import numpy as np
import re

def has_pattern(s, pattern):
    if pd.isna(s):
        return None
    s = s.lower().replace(" ", "")  # Nettoyage simple
    return int(bool(re.search(pattern, s)))


def count_anomalies(text, keyword):
    if pd.isna(text):
        return 0
    return len(re.findall(rf'\b{keyword}', text))

def is_pattern(protein_change, pattern):

    if isinstance(protein_change, str):
        return pattern in protein_change
    return False

def has_complex(protein_change):
    if isinstance(protein_change, str):
        # 1. cas avec underscore suivi de "del" ou "ins" ou autres types explicites
        pattern1 = r'p\.[A-Z]\d+_[A-Z]\d+(del|ins|dup)[A-Z]*'
        
        # 2. cas d’acronymes avec underscore comme MLL_PTD, FLT3_ITD
        pattern2 = r'^[A-Z0-9]+_[A-Z0-9]+$'
        
        return bool(re.search(pattern1, protein_change)) or bool(re.search(pattern2, protein_change))
    return False