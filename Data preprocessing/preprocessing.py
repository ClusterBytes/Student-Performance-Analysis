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
                        
output_features = ['Year','Dept_CSE', 'Dept_Civil', 'Dept_ECE',
                    'Dept_EEE', 'Dept_IT', 'Dept_MECH', 'S1_1', 'S1_2', 'S1_3',
                    'S1_4', 'S1_5', 'S1_6', 'S2_1', 'S2_2', 'S2_3', 'S2_4', 'S3_1', 
                    'S3_2', 'S3_3', 'S3_4', 'S3_5', 'S3_6', 'S4_1', 'S4_2', 'S4_3', 
                    'S4_5', 'S4_6', 'S5_1', 'S5_2', 'S5_3', 'S5_4', 'S6_5', 'S6_1', 
                    'S6_2', 'S6_3', 'S7_1', 'S7_2', 'S7_3', 'S7_4', 'S7_5', 'A1', 
                    'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'I1', 'I2', 'I3', 'I4', 
                    'I5', 'I6', 'I7', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7']




transformed=ct.fit_transform(data)

transformed_data = pd.DataFrame(transformed, columns = output_features)

print(transformed_data)

#print(ct.get_feature_names_out())

transformed_data.to_csv("result.csv")