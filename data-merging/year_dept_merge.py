from pandas import *

# def year_dept_merge(data):    
# reading CSV file


data = read_csv("1.csv")
df = DataFrame(data)

# df2 = DataFrame(data)

column_to_compare = 'Reg_No'


df = df.loc[:, ['Reg_No','Dept',]]

df = df.drop_duplicates()

duplicates = df[df.duplicated(subset=column_to_compare, keep=False)]


df.to_csv("Grouped.csv",index=False)



# # column_to_count = 'Year'
# subjects_per_year = df2.groupby(['Reg_No', 'Year'])['Subject'].count()



# print(subjects_per_year)

# return df


