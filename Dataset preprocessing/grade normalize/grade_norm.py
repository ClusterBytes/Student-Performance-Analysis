import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder


par='../../Dataset/CSV-Subject'
col=['reg','sem','year','branch','sub','attendance','internals','grade']
year=['2015','2016','2017','2018']
sem=['S1','S2']
dept=['CSE','Civil','MECH','IT','ECE','EEE']
grade=['F','P','C','B','B+','A','A+','S']

for _year in year:
    for s in sem:
        for d in dept:
            dir=par+'/'+_year+'/'+s+'/'+d
                
            for f in os.listdir(dir):
                print('file',dir,f)
                data=pd.read_csv(dir+'/'+f,header=None,names=col)
                
                
                y=[]
                for g in grade:
                    y.append(data.loc[data['grade']==g,'grade'].count())
                y=np.array(y)
                
                new_grade={'B+':['B+','B'],
                            'B':['C+','C'],
                            'C':['D','P'],
                            'P':['F','F']}


                perc={}
                for g in range(2,5):
                    Grade=grade[g]
                    
                    b1=(3*y[g]+y[g+1]-y[g-1])//6
                    b2=b1+1
                    a1=y[g]-b1
                    a2=y[g]-b2
                    
                    perc[Grade]=b1 if (b1-a1)-(y[g+1]-y[g-1])<(b2-a2)-(y[g+1]-y[g-1]) else b2
                perc['P']=y[1]
                
                
                print(y)
                print(new_grade)
                print(perc)
                
                for g in range(1,5):
                    Grade=grade[g]
                    slice_index=int(perc[Grade])
                    print(Grade,perc[Grade])
                    c_indices=data.loc[data['grade']==Grade].index[:slice_index]
                    data.loc[c_indices,'grade']=new_grade[Grade][0]
                    data.loc[data['grade']==Grade,'grade']=new_grade[Grade][1]
                    
                data.to_csv(dir+'/'+'norm_'+f+'.csv',index=False,header=False)
                
                