'''
# THIS FILE CONTAINS THE MAIN STUFF NEEDED FOR ENCODING A MULTILABEL COLUMN.
# WHICH IS A CALSS CONTAINING TWO METHODS
# THE FIRST ONE IS THE UNIQUE LABELS EXTRACTOR WHICH EXTRACTS ALL THE UNIQUE LABELS IN THE MULTILABEL COLUMN
# THE SECOND METHOD IS THE ENCODER, WHICH ENCODES THE MULTILABEL COLUMN AND RETURNS A OHE LIST FOR EACH ENTRY (ROW) IN THE MULTILABEL COLUMN
'''
import pandas as pd

class MultiLabelEncoder():
    def __init__(self, multilabel_column:pd.Series, unique_labels:set=set(), delimiter:str=','):
        self.mlc = multilabel_column.dropna() #we don't want no missing values over here\
        self.unique_labels = unique_labels
        self.delimiter = delimiter
        self.encodings = None
    
    def extract_unique_labels(self, ):
        unique_categories = self.mlc.unique()

        for cat in unique_categories:
            if isinstance(cat, str): # NOTE I WOULD PROBABLY NEED TO ADD HANDLERS FOR OTHER DATATYPES...
                if self.delimiter in cat:
                    row_cats = cat.split(self.delimiter)
                    for row_cat in row_cats:
                        self.unique_labels.add(row_cat)
                else:
                    self.unique_labels.add(row_cat)
        return
    
    def multilabel_oh_encode(self):
        label_to_int = dict((label, index) for index, label in enumerate(self.unique_labels))
        label_encoded = [[label_to_int[label] for label in row.split(self.delimiter) ] for row in self.mlc]

        #create one hot list
        ohe_list = list()

        if len(self.unique_labels) == 0:
            raise ValueError('No unique labels, have you tried calling the `extract_unique_labels` method?')

        for row in label_encoded:
            row_enc = [0 for _ in range(len(self.unique_labels))]
            for label in row:
                row_enc[label] = 1
            ohe_list.append(row_enc)

        self.encodings = pd.Series(ohe_list)
        return 