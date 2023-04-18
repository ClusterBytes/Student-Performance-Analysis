import pandas as pd

data=pd.read_csv("../Dataset/CSV-Single/4_subjects_unified.csv")

subs=data['Subject'].unique()
studs=data['Reg_No'].unique()
new_cols=['Dept']

for c in subs:
    new_cols.append(c+'_mark')
    new_cols.append(c+'_att')
    new_cols.append(c+'_grade')
    
new_data=pd.DataFrame(index=studs,columns=new_cols)

count=0

for i in range(data.shape[0]):

    reg=data.iloc[i]['Reg_No']
    dept=data.iloc[i]['Dept']
    sub=data.iloc[i]['Subject']
    mark=data.iloc[i]['Internal mark']
    att=data.iloc[i]['Attendance']
    grade=data.iloc[i]['Grade']
    
    new_data.loc[reg,'Dept']=dept
    new_data.loc[reg,sub+'_mark']=mark
    new_data.loc[reg,sub+'_att']=att
    new_data.loc[reg,sub+'_grade']=grade
    
    count+=1
    if(count%250==0):
        print(str(count)+'/'+str(data.shape[0]))


new_data.to_csv('../Dataset/CSV-Single/5_3sub_1stud.csv',index_label='Reg_No')