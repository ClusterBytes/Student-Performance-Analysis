import pandas  as pd

df = pd.read_csv("3_grade_normalized.csv")
slotted_df=pd.read_csv("slotting_with_0.csv")
def year_dept_merge(df):

    df = df.loc[:, ["Reg_No", "Dept"]]

    df = df.drop_duplicates()

    df_filtered = df[(df["Reg_No"] != "KSD17ME045") | (df["Dept"] != "IT")]
    df_filtered = df_filtered.sort_values('Reg_No', ascending=True)
   
    # df_filtered.to_csv("Grouped.csv", index=False)
    return df_filtered
df_filtered =year_dept_merge(df)

merged_df = pd.merge(df_filtered,slotted_df, on='Reg_No', how='outer')
merged_df=merged_df.set_index('Reg_No',drop=True)
merged_df.to_csv('dataset_v2.csv')
print(merged_df)