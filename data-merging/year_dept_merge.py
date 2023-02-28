from pandas import *

# def year_dept_merge(data):    
# reading CSV file


data = read_csv("1.csv")
df = DataFrame(data)

column_to_compare = 'Reg_No'

df = df.loc[:, ['Reg_No', 'Year', 'Dept']]

df = df.drop_duplicates()

duplicates = df[df.duplicated(subset=column_to_compare, keep=False)]


df.to_csv("Grouped.csv",index=False)
# return df


