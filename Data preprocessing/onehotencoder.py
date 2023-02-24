import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Datasets/1.csv')
data1 = data.loc[(data['Dept']=='CSE') & (data['Semester']=='S1') & (data['Year']==2015)]
print(data1)
ct = ColumnTransformer([('others1','passthrough',slice(4)),
                        ('onehot', OneHotEncoder(),['Subject']),
                     ],remainder='passthrough')
transformed=ct.fit_transform(data1)
print(transformed[100:120])