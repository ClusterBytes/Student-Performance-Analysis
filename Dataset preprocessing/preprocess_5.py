import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer

data=pd.read_csv('../Dataset/CSV-Single/5_3sub_1stud.csv')

oe=OrdinalEncoder(categories=[['F','P','D','C','C+','B','B+','A','A+','S']]*13,handle_unknown='use_encoded_value',unknown_value=np.nan)
ohe=OneHotEncoder(sparse_output=False)

ct=ColumnTransformer(transformers=[
    ('reg','passthrough',['Reg_No']),
    ('dept',ohe,['Dept']),
    ('mark_att','passthrough',slice(2,28)),
    ('grades',oe,slice(28,41))
])

print('Transforming.....')
new_data_numpy=ct.fit_transform(data)
print('Transformed..... Writing into 5_1.csv')

ohe_cols=ct.named_transformers_['dept'].categories_

cols=data.columns
new_cols=['Reg_No']
for c in ohe_cols[0]:
    new_cols.append(c)
for i in range(2,len(cols)):
    new_cols.append(cols[i])

new_data=pd.DataFrame(new_data_numpy,columns=new_cols)

new_data.replace(np.nan,0,inplace=True)

new_data.to_csv('../Dataset/CSV-Train/5_1.csv',index=False)