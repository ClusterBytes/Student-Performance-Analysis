import pandas as pd
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
gp=[{  #2019 
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
},{   #2015
	'F':0,
	'P':4,
	'C':5,
	'B':6,
	'B+':7,
	'A':8,
	'A+':9,
	'S':10,
}]

def sgpa(credit,gp,temp_df,t_cred):
    sgpa=0
    for index, row in temp_df.iterrows():
        temp_cred=credit[row['Subject']]
        temp_gp=gp[row['Grade']]
        sgpa+=(temp_cred*temp_gp)
    
    return sgpa/t_cred
    

df=pd.read_csv("../Dataset/CSV-Single/2_no_unwanted_grades.csv")
unique_reg_nos = set(df['Reg_No'])
new_df=pd.DataFrame(columns=['Reg_No','SGPA_1','SGPA_2'])

#every BE100(Mechanics) in S1 and every BE110(Graphics) in S2
df.loc[df['Subject']=='BE100','Semester']='S1'
df.loc[df['Subject']=='BE110','Semester']='S2'

count=0
perc=0
total=len(unique_reg_nos)

for reg_no in unique_reg_nos:
    temp_df_s1=df.loc[df['Reg_No']==reg_no].loc[df['Semester']=='S1']
    temp_df_s2=df.loc[df['Reg_No']==reg_no].loc[df['Semester']=='S2']
    
    try:
        if temp_df_s1.iloc[0][2]<2019:
            sgpa_1=sgpa(credit,gp[1],temp_df_s1,24)
            sgpa_2=sgpa(credit,gp[1],temp_df_s2,23)
        else :
            sgpa_1=sgpa(credit,gp[0],temp_df_s1,17)
            sgpa_2=sgpa(credit,gp[0],temp_df_s2,21)
    except Exception as e:
        print(e,reg_no)
        sgpa_1=0
        sgpa_2=0
    
    temp_new_df=pd.DataFrame(columns=['Reg_No','SGPA_1','SGPA_2'])
    temp_new_df.loc[0]=[reg_no,sgpa_1,sgpa_2]
    new_df=pd.concat([new_df,temp_new_df],axis=0)
	
    count+=1
    if (count/total)*10 > perc:
        print(str(count)+'/'+str(total)+'... '+str(round((count/total)*100,2))+'%')
        perc+=1

new_df.to_csv('../Dataset/CSV-Single/6_sgpa1_sgpa2.csv',index=False)