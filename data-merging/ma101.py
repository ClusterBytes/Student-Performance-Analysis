import pandas as pd
import numpy as np
import functools as ft


data = pd.read_csv('result.csv')

columns_to_keep = ["Reg_No","A32","I32","G32"]

new_df = data[columns_to_keep]

print(new_df)
new_df.to_csv("only mat.csv", index=False)