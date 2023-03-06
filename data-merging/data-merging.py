import pandas as pd
import numpy as np
import functools as ft

from year_dept_merge import year_dept_merge

df = pd.read_csv("1.csv")

merging_columns = ["Subject", "Attendance", "Internal mark", "Grade"]
final = []
# for each student merge the grade,attendance and internal
for col in merging_columns:
    grouped = df.groupby("Reg_No")[col].apply(list)
    grouped_df = pd.DataFrame(grouped.values.tolist(), index=grouped.index)
    columns = list(grouped_df.columns)
    new_cols = [col[0:1] + str(i + 1) for i in range(len(columns))]
    grouped_df.columns = new_cols
    final.append(grouped_df)

# merge the dept of each student
year_dept = year_dept_merge(df)
year_dept.set_index("Reg_No")
year_dept.sort_values("Reg_No")
final.insert(0, year_dept)

# final csv with reg_no,dept,subject,attendance,internal,grade
df_final = ft.reduce(lambda left, right: pd.merge(left, right, on="Reg_No"), final)
df_final.to_csv("each_student_row.csv", index=False)
