import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

f1='../Dataset/CSV-Single/2_no_unwanted_grades.csv'
f3='../Dataset/CSV-Single/3_grade_normalized.csv'
grade=['F','P','D','C','C+','B','B+','A','A+','S']

data_o=pd.read_csv(f1)
data_n=pd.read_csv(f3)

i=0
if len(sys.argv)==2:
    values=data_o[sys.argv[1]].unique()
else :
    values=[]
    values.append(sys.argv[2])

sns.set()
palette=sns.blend_palette(['#FF2C2C','#51FF51'],n_colors=10)

for val in values:
    data_org=data_o.loc[(data_o[sys.argv[1]]==val) & (data_o['Year']<2019)]
    data_norm=data_n.loc[(data_n[sys.argv[1]]==val) & (data_n['Year']<2019)]
    
    if data_org.shape[0]>0 and data_norm.shape[0]>0:
    
        fig,axs=plt.subplots(1,2,figsize=(12,5))
        axs[0].set_title('2015 Scheme')
        axs[1].set_title('2019 Scheme')
        axs[1].tick_params()
        fig.suptitle(val)
        
        sns.countplot(ax=axs[0],data=data_org, x="Grade", palette=palette,order=grade)
        sns.countplot(ax=axs[1],data=data_norm, x="Grade",palette=palette,order=grade)
        
        y_lims_0=axs[0].get_ylim()
        y_lims_1=axs[1].get_ylim()
        axs[0].set_ylim(y_lims_1) if y_lims_1>y_lims_0 else axs[1].set_ylim(y_lims_0)
        plt.show()
    
    # if i==0:
        # break
    # i+=1
    
    