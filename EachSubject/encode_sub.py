import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.base import BaseEstimator, TransformerMixin
import sys


class DivideByHundred(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_100 = X / 100
        return X_100

    def get_feature_names_out(self, features=None):
        return features

if ( sys.argv[3]=="true"):
    data = pd.read_csv("filtered_"+sys.argv[1] + ".csv")
else:
    data = pd.read_csv(sys.argv[1] + ".csv")
# data =data.head()
data.set_index(data["Reg_No"], inplace=True)
print("total rows ",data.shape[0])
onehot_encode = OneHotEncoder(sparse_output=False)
ordinal_encode_year = OrdinalEncoder()
ordinal_encode_grade = OrdinalEncoder(categories=[["F", "P", "D", "C", "C+", "B", "B+", "A", "A+", "S"]])
scale_attendance = DivideByHundred()
scale_internal = DivideByHundred()
position = sys.argv[2]
ct = ColumnTransformer(
    [
        ("Reg", "passthrough", ["Reg_No"]),
        ("Attendance", scale_attendance, ["A" + position]),
        ("Internal", scale_internal, ["I" + position]),
        ("Grade", ordinal_encode_grade, ["G" + position]),
    ]
)

transformed = ct.fit_transform(data)

transformed_col_name = ct.get_feature_names_out()
col_name = transformed_col_name.tolist()

new_col = []
for col in col_name:
    if "Reg__" in col:
        column = col.replace("Reg__", "")
    elif "Dept__" in col:
        column = col.replace("Dept__", "")
    elif "Sub__" in col:
        column = col.replace("Sub__", "")
    elif "Attendance__" in col:
        column = col.replace("Attendance__", "")
    elif "Internal__" in col:
        column = col.replace("Internal__", "")
    else:
        column = col.replace("Grade__", "")
    new_col.append(column)

transformed_data = pd.DataFrame(transformed, columns=new_col)

transformed_data.to_csv(sys.argv[1] + "_encode.csv", index=False)
print("encoded the subject " + sys.argv[1])
