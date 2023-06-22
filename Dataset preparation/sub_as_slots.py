import pandas as pd
import numpy as np

slots=pd.read_csv("asset/slot_wise.csv",header=None)
data=pd.read_csv("../Dataset/CSV-Single/3_grade_normalized.csv")

new_header = slots.iloc[2]
slots = slots[3:]
data.columns = new_header

# Now your DataFrame has the desired structure
print(data.head())
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