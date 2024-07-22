Simple Tool For Encoding Multilabeled Columns

How to use:

The `MultiLabelEncoder` class from `main.py`, takes care of encoding the multilabeled column.

To use, create a `MultiLabelEncoder` object, parameters are:  

`multilabel_column` type: pd.Series
`unique_labels` type:set [optional]
`delimiter` type:str [optional]

As of 22.07.2024 the Encoder works best for csv files, where the columns are strings.
Typically looking like this:

TAGS
"Factory Tuner,Luxury,High-Performance"
"Luxury,Performance"
"Luxury,High-Performance"

Here the delimiter is a comma ','

For sample usage, check out thte `mlc.ipynb` notebook
Thank you (^_^ )