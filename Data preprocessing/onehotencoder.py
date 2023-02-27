import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Datasets/reordered.csv')

year_dept = ['Year','Dept']
subjects = ['S1','S2', 'S3', 'S4', 'S5', 'S6', 'S7']

onehot_encode = Pipeline(steps = [('encoder', OneHotEncoder(sparse_output=False))])

ct = ColumnTransformer([('noencoder', 'passthrough', year_dept),
                        ('onehot', onehot_encode, subjects)],
                        remainder='passthrough')
transformed=ct.fit_transform(data)

transformed_data = pd.DataFrame(transformed, columns = ct.get_feature_names_out())

transformed_data.to_csv("result.csv")