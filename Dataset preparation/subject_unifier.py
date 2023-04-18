import pandas as pd
import numpy as np

def custom_round(mark):
    if mark>=90:
        return 95
    new_mark=mark*100
    first=new_mark//1000
    last=750 if new_mark%1000>=500 else 250
    final=(first*1000)+last
    return final/100
    
data=pd.read_csv("../Dataset/CSV-Single/3_grade_normalized.csv")
new_sub={
    'BE100':'EST100',
    'BE110':'EST110',
    'CS100':'EST102',
    'CS110':'CS120',
    'CY100':'CYT100',
    'CY110':'CYL120',
    'MA101':'MAT101',
    'MA102':'MAT102',
    'PH100':'PHT100',
    'PHT110':'PHT100',
    'PH110':'PHL120',
    'BE10105':np.nan,
    'BE102':np.nan,
    'BE103':np.nan,
    'HUN101':np.nan,
    'HUN102':np.nan,
    'EC100':'EST130',
    'EE100':np.nan,
    'BE10103':np.nan,
    'BE10104':'EST130',
    'EE110':np.nan,
    'EC110':'ESL130',
    'BE10101':np.nan,
    'CE100':np.nan,
    'ME100':'EST120',
    'BE10102':'EST120',
    'ME110':'ESL120',
    'CE110':np.nan
}
add_to={
    'EE100':'EC100',
    'BE10103':'BE10104',
    'EE110':'EC110',
    'BE10101':'BE10102',
    'CE100':'ME100',
    'CE110':'ME110'
}
g_m={
    'S':95,
    'A+':87.5,
    'A':82.5,
    'B+':77.5,
    'B':72.5,
    'C+':67.5,
    'C':62.5,
    'D':57.5,
    'P':52.5,
}

def avg_grade(grade,c_grade):
    global g_m
    avg_m=custom_round((g_m[c_grade]+g_m[grade])/2)
    for g in g_m:
        if(g_m[g]==avg_m):
            return g

print('====  merging some subjects  ====')
count=0
for i in add_to:
    stud=data.loc[data['Subject']==i]
    
    for j in range(stud.shape[0]):
        att=stud.iloc[j,5]
        mark=stud.iloc[j,6]
        grade=stud.iloc[j,7]
        reg=stud.iloc[j,0]
        
        corr=data.loc[(data['Reg_No']==reg) & (data['Subject']==add_to[i])]
        index=corr.index
        
        if len(index)==1:
            c_att=corr.iloc[0,5]
            c_mark=corr.iloc[0,6]
            c_grade=corr.iloc[0,7]
            
            n_att=(c_att+att)/2
            n_mark=(c_mark+mark)/2
            if c_grade=='F' or grade=='F':
                n_grade='F'
            else :
                n_grade=avg_grade(grade,c_grade)
            
            data.loc[index,'Subject']=new_sub[add_to[i]]
            data.loc[index,'Attendance']=n_att
            data.loc[index,'Internal mark']=n_mark
            data.loc[index,'Grade']=n_grade
            
            
    count+=1
    print(str(count)+'/'+str(len(add_to)),'Completed :',i)
    

to_nan=['EC100','BE10104','EC110','ME100','BE10102','ME110']
for i in to_nan:
    new_sub[i]=np.nan
    
print('====  converting subject codes  ====')
count=0
for i in new_sub:
    index=data.loc[data['Subject']==i].index
    data.loc[index,'Subject']=new_sub[i]
    count+=1
    print(str(count)+'/'+str(len(new_sub)),'Completed :',i)

print('====  dropping unwanted subjects  ====')
data.dropna(inplace=True)

print('writing to ........... 4_subjects_unified.csv')
data.to_csv('../Dataset/CSV-Single/4_subjects_unified.csv',index=False)