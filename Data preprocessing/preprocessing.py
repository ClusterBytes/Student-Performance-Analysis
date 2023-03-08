import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.base import BaseEstimator, TransformerMixin

class DivideByHundred(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X_100 = X/100
        return X_100
    
    def get_feature_names_out(self, features=None):
        return features
        
data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/data-merging/removed.csv')

data.set_index(data['Reg_No'], inplace=True)

onehot_encode = OneHotEncoder(sparse_output=False)
ordinal_encode_year = OrdinalEncoder()
ordinal_encode_grade = OrdinalEncoder(categories=[['F', 'P', 'D', 'C', 'C+', 'B', 'B+', 'A', 'A+', 'S']] * 18)
scale_attendance = DivideByHundred()
scale_internal = DivideByHundred()

ct = ColumnTransformer([('Reg','passthrough',['Reg_No']),
                        ('Dept', onehot_encode, ['Dept']),
                        ('Sub', onehot_encode, slice(2,20)),
                        ('Attendance', scale_attendance, slice(20,38)),
                        ('Internal', scale_internal, slice(38,56)),
                        ('Grade', ordinal_encode_grade, slice(56,74))])

transformed=ct.fit_transform(data)

transformed_col_name = ct.get_feature_names_out()
col_name = transformed_col_name.tolist()

new_col = []
for col in col_name:
    if('Reg__' in col):
        column = col.replace('Reg__','')
    elif('Dept__' in col):
        column = col.replace('Dept__','')
    elif('Sub__' in col):
        column = col.replace('Sub__','')
    elif('Attendance__' in col):
        column = col.replace('Attendance__','')
    elif('Internal__' in col):
        column = col.replace('Internal__','')
    else:
        column = col.replace('Grade__','')
    new_col.append(column)

transformed_data = pd.DataFrame(transformed, columns = new_col)

print(transformed_data)

transformed_data.to_csv("result.csv", index=False)