import pandas as pd
import numpy as np

def bin_data(value):
    if value==0:
        return value
    if value==1.0:
        return 0.95
    value*=100
    value=value//10
    value+=0.5
    return value/10

data=pd.read_csv('../Dataset/CSV-Train/5_1.csv')
data.replace(np.nan,0,inplace=True)

for col in data.columns:
    if ('_mark' in col) or ('_att' in col):
        data[col] = data[col].apply(bin_data)

data.to_csv('../Dataset/CSV-Train/5_2_binned.csv',index=False)