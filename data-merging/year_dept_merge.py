from pandas import *


def year_dept_merge(df):

    df = df.loc[:, ["Reg_No", "Dept"]]

    df = df.drop_duplicates()

    df_filtered = df[(df["Reg_No"] != "KSD17ME045") | (df["Dept"] != "IT")]

    # df_filtered.to_csv("Grouped.csv", index=False)
    return df_filtered
