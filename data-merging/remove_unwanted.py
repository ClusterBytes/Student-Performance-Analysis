import pandas as pd
import numpy as np
import functools as ft


df = pd.read_csv("each_student_row.csv")
# for i in range(1, 19):

# print(df["G" + str(i)])
# df_filtered = df[(df["G" + str(i)] != "Withheld")]

# df.loc[(df["G" + str(i)] == "Withheld")]
removing_items = ["Withheld", "Withheld*", "FE", "I", "Absent", "Debarred"]
for item in removing_items:
    df.replace(item, "F", inplace=True)

print(df)

df.to_csv("removed.csv", index=False)
