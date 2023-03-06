import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

class DivideByHundred(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X_100 = X/100
        return X_100
        

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Datasets/reordered.csv')

onehot_encode = OneHotEncoder(sparse_output=False)
ordinal_encode_year = OrdinalEncoder()
ordinal_encode_grade = OrdinalEncoder(categories=[['F', 'P', 'D', 'C', 'C+', 'B', 'B+', 'A', 'A+', 'S']] * 7)
scale_attendance = DivideByHundred()
scale_internal = DivideByHundred()


ct = ColumnTransformer([('Year', ordinal_encode_year, ['Year']),
                        ('Dept', onehot_encode, ['Dept']),
                        ('Sub', onehot_encode, slice(2,9)),
                        ('Attendance', scale_attendance, slice(9,16)),
                        ('Internal', scale_internal, slice(16,23)),
                        ('Grade', ordinal_encode_grade, slice(23,30))])

transformed=ct.fit_transform(data)

transformed_data = pd.DataFrame(transformed, columns = ct.get_feature_names_out())

print(transformed_data)

transformed_data.to_csv("result.csv")