'''
# THIS FILE CONTAINS THE MAIN STUFF NEEDED FOR ENCODING A MULTILABEL COLUMN.
# WHICH IS A CALSS CONTAINING TWO METHODS
# THE FIRST ONE IS THE UNIQUE LABELS EXTRACTOR WHICH EXTRACTS ALL THE UNIQUE LABELS IN THE MULTILABEL COLUMN
# THE SECOND METHOD IS THE ENCODER, WHICH ENCODES THE MULTILABEL COLUMN AND RETURNS A OHE LIST FOR EACH ENTRY (ROW) IN THE MULTILABEL COLUMN
'''

import numpy as np
import pandas as pd



class MultiLabelEncoder():
    def __init__(self, multilabel_column:pd.Series, unique_labels:set=set(), delimiter:str=','):
        self.mlc = multilabel_column
        self.unique_labels = unique_labels
        self.delimiter = delimiter
    
    def extract_unique_labels(self, ):
        unique_categories = self.mlc.unique()

        for cat in unique_categories:
            if isinstance(cat, 'str'): # NOTE I WOULD PROBABLY NEED TO ADD HANDLERS FOR OTHER DATATYPES...
                if self.delimiter in cat:
                    row_cats = cat.split(self.delimiter)
                    for row_cat in row_cats:
                        self.unique_labels.add(row_cat)
                else:
                    self.unique_labels.add(row_cat)
    
    def multilabel_oh_encode(self):
        label_to_int = dict((label, index) for index, label in enumerate(self.unique_labels))