import pandas as pd
import numpy as np
import functools as ft

from year_dept_merge import year_dept_merge

df = pd.read_csv("3_grade_normalized.csv")
print(df["Reg_No"])
merging_columns = ["Subject", "Attendance", "Internal mark", "Grade"]
final = []
gpy = df.groupby("Reg_No")["Subject"].apply(list)
gp = pd.DataFrame(gpy.values.tolist(), index=gpy.index)

# print(gp)
# for each student merge the grade,attendance and internal
for col in merging_columns:
    grouped = df.groupby("Reg_No")[col].apply(list)
    grouped_df = pd.DataFrame(grouped.values.tolist(), index=grouped.index)
    columns = list(grouped_df.columns)
    new_cols = [col[0:1] + str(i + 1) for i in range(len(columns))]
    grouped_df.columns = new_cols

    if col == "Subject":
        grouped_df.fillna(value="NOSUB", inplace=True)
    if col == "Grade":
        grouped_df.fillna(value="F", inplace=True)
    else:
        grouped_df.fillna(value=0, inplace=True)

    final.append(grouped_df)


# merge the dept of each student
year_dept = year_dept_merge(df)
year_dept.set_index("Reg_No")
year_dept.sort_values("Reg_No")
final.insert(0, year_dept)

# final csv with reg_no,dept,subject,attendance,internal,grade
df_final = ft.reduce(lambda left, right: pd.merge(left, right, on="Reg_No"), final)
# print(df_final)
df_final.to_csv("each_student_row.csv", index=False)
