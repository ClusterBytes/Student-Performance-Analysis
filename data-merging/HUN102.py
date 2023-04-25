import pandas as pd
import numpy as np
import functools as ft


data = pd.read_csv('dataset_v2.csv')

columns_to_keep = ["Reg_No","HUN102","A31","I31","G31"]

new_df = data[columns_to_keep]

print(new_df)
new_df.to_csv("HUN102.csv", index=False)