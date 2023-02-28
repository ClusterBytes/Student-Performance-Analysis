import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder


dir='../Dataset/CSV-Subject/2015'
col=['reg','sem','year','branch','sub','attendance','internals','grade']


for f in os.listdir(dir):
    #print('file',f)
    data=pd.read_csv(dir+'/'+f,header=None,names=col)
    
    OE_grade=OrdinalEncoder(categories=[['F','P','C','B','B+','A','A+','S']])
    CT=ColumnTransformer([
        ('pass','passthrough',slice(1)),
        ('grades',OE_grade,['grade'])
    ],sparse_threshold=0)
    
    data_tr=pd.DataFrame(CT.fit_transform(data),columns=['reg','grade'])
    
    count=data_tr.groupby(['grade'],observed=True).count()
    count.columns=['count']

    X=np.array([x for x in range(8)])
    y=[]
    for x in X:
        try:
            y.append(count['count'][x])
        except KeyError:
            y.append(0)
    y=np.array(y)
    
    fig,axs = plt.subplots(1,2, figsize=(9, 3))     
    axs[0].bar(X,y)
    axs[1].plot(X,y)
    fig.suptitle(f)
    plt.show()
    
    # print(count)
    # print(type(X),X)
    # print(type(y),y)
    