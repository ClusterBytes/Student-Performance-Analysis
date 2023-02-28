import pandas as pd
import numpy as np
import functools as ft

df = pd.read_csv("1.csv")

merging_columns = ["Subject", "Attendance", "Internal mark", "Grade"]
final = []
for col in merging_columns:
    grouped = df.groupby("Reg_No")[col].apply(list)
    grouped_df = pd.DataFrame(grouped.values.tolist(), index=grouped.index)
    columns = list(grouped_df.columns)
    new_cols = [col[0:1] + str(i + 1) for i in range(len(columns))]
    grouped_df.columns = new_cols
    final.append(grouped_df)
    print(grouped_df)

df_final = ft.reduce(lambda left, right: pd.merge(left, right, on="Reg_No"), final)
df_final.to_csv("final.csv", index=True)
