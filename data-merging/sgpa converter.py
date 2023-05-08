import pandas as pd

df = pd.read_csv('3_grade_normalized.csv')

credit={
	'BE100':4,
	'BE10101':3,
	'BE10102':3,
	'BE10103':3,
	'BE10104':3,
	'BE10105':3,
	'BE102':3,
	'BE103':3,
	'BE110':3,
	'CE100':3,
	'CE110':1,
	'CS100':3,
	'CS110':1,
	'CS120':1,
	'CY100':4,
	'CY110':1,
	'CYL120':1,
	'CYT100':4,
	'EC100':3,
	'EC110':1,
	'EE100':3,
	'EE110':1,
	'ESL120':1,
	'ESL130':1,
	'EST100':3,
	'EST102':4,
	'EST110':3,
	'EST120':4,
	'EST130':4,
	'HUN101':0,
	'HUN102':0,
	'MA101':4,
	'MA102':4,
	'MAT101':4,
	'MAT102':4,
	'ME100':3,
	'ME110':1,
	'PH100':4,
	'PH110':1,
	'PHL120':1,
	'PHT100':4,
	'PHT110':4,
}



gp={
	'F':0,
	'P':5.5,
	'D':6.0,
	'C':6.5,
	'C+':7.0,
	'B':7.5,
	'B+':8.0,
	'A':8.5,
	'A+':9.0,
	'S':10.0,
}
unique_reg_nos = set(df['Reg_No'])
count=0
sum=0
for reg_no in unique_reg_nos:
    temp_df_s1=df.loc[df['Reg_No']==reg_no].loc[df['Semester']=='S1']
    temp_df_s2=df.loc[df['Reg_No']==reg_no].loc[df['Semester']=='S2']
    print(temp_df_s1)
    print(temp_df_s2)
    
	 # Calculate SGPA for semester 1
    s1_credits = []
    s1_gpoints = []
    for index, row in temp_df_s1.iterrows():
        print(index,row)
        credit_points = credit.get(row['Subject'], 0)
        grade_points = gp.get(row['Grade'], 0)
        s1_credits.append(credit_points)
        s1_gpoints.append(grade_points)

    print(credit_points)
	
    break
#     count+=1

# print(count)