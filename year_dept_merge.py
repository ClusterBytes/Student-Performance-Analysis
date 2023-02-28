from pandas import *

def year_dept_merge(data):    
    # reading CSV file
    # data = read_csv("1.csv")
    df = DataFrame(data)

    df = df.loc[:, ['Reg_No', 'Year', 'Dept']]
    df = df.drop_duplicates()
    # df.to_csv("Grouped_csv",index=False)
    return df

