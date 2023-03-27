import pandas as pd
import numpy as np

sub_list = [
    "BE100",
    "BE10101",
    "BE10102",
    "BE10103",
    "BE10104",
    "BE10105",
    "BE102",
    "BE103",
    "BE110",
    "CE100",
    "CE110",
    "CS100",
    "CS110",
    "CS120",
    "CY100",
    "CY110",
    "CYL120",
    "CYT100",
    "EC100",
    "EC110",
    "EE100",
    "EE110",
    "ESL120",
    "ESL130",
    "EST100",
    "EST102",
    "EST110",
    "EST120",
    "EST130",
    "HUN101",
    "HUN102",
    "MA101",
    "MA102",
    "MAT101",
    "MAT102",
    "ME100",
    "ME110",
    "PH100",
    "PH110",
    "PHL120",
    "PHT100",
    "PHT110",
]

# print(sub_list)

import pandas as pd
import numpy as np
import functools as ft

from year_dept_merge import year_dept_merge

df = pd.read_csv("3_grade_normalized.csv")
# print(df["Reg_No"])
df_pivot = df.pivot(index=None, columns="Subject", values="Attendance")

df_pivot["Reg_No"] = df["Reg_No"]
df_pivot = df_pivot.reindex(columns=["Reg_No"] + list(df_pivot.columns[:-1]))

df_grouped = df_pivot.groupby("Reg_No").mean()

for index, row in df_grouped.iterrows():
    for sub in sub_list:
        if np.isnan(row[sub]):
            df_grouped.loc[index, sub] = 0
        else:
            df_grouped.loc[index, sub] = 1
sub_columns = df_grouped.columns
# print(df_grouped)
attendance_col = []
internal_col = []
grade_col = []


for i in range(1, len(sub_list)):
    attendance_col.append(f"A{i}")
    internal_col.append(f"I{i}")
    grade_col.append(f"G{i}")
final_col = attendance_col + internal_col + grade_col

c_ob = {}
for i in final_col:
    c_ob[i] = pd.Series(dtype="float64")

df_grouped = df_grouped.assign(**c_ob)
# df_grouped = df_grouped.head(5)
# with_new_col = df_grouped.reindex(columns=final_col)

count = 0
for new_index, new_row in df_grouped.iterrows():
    count += 1
    print("completed: ", round((count / 2316) * 100, 3), "%")
    print("done:", new_index)
    for index, row in df.iterrows():
        if row["Reg_No"] == new_index:
            for i, sub in enumerate(sub_list, start=1):
                if row["Subject"] == sub:
                    df_grouped.loc[row["Reg_No"], f"A{i}"] = row["Attendance"]
                    df_grouped.loc[row["Reg_No"], f"I{i}"] = row["Internal mark"]
                    df_grouped.loc[row["Reg_No"], f"G{i}"] = row["Grade"]

# print(i)


df_grouped.to_csv("slotting.csv", index=True)
