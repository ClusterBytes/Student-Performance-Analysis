import pandas as pd
import numpy as np

df = pd.read_csv("1.csv")
df_pivot = pd.pivot_table(
    df, values=["Subject", "Attendance", "Internal mark", "Grade"], index="Reg_No", aggfunc=list, sort=False
)
print(df_pivot.columns)
df_pivot.to_csv("pivot_table.csv", index=True)

grouped = df.groupby("Reg_No")["Subject"].apply(list)
grouped = df.groupby("Reg_No")["Attendance"].apply(list)
# Create a new DataFrame with the lists as columns, with names s1, s2, s3, etc.
df_new = pd.DataFrame(grouped.values.tolist(), index=grouped.index).add_prefix("S")
df_ne = pd.DataFrame(grouped.values.tolist(), index=grouped.index).add_prefix("A")
print(df_ne)
# Reset the index to make the grouping column a regular column
# df_new = df_new.reset_index()

# df_pivot.columns = [f"s{i}" for i in range(1, len(df_pivot.columns.unique(level=0)) + 1)]

# for (colName, colData) in df.iteritems():
#     print(colName)
# "Attendance", "Internal mark", "Grade"
# import csv

# with open("merged.csv", mode="w") as merged_file:
#     writer = csv.writer(merged_file)
#     writer.writerow(["Reg_No"])
#     with open("1.csv", mode="r") as file:
#         print(type(file))
#         csvFile = csv.DictReader("1.csv")
#         csvFie = csv.DictReader("1.csv")

#         eachRow = []
#         print("dss", csvFile)
#         for lines in csvFile:

#             print(lines)
#             # if lines["Reg_No"] not in eachRow:
#             #     eachRow.append(lines["Reg_No"])
#             #     writer.writerow([lines["Reg_No"]])

#         # for reg in eachRow:
#         print("dsds", csvFile)
#         for line in csvFie:
#             print(line)
