import pandas as pd
import sys

df=pd.read_csv('/home/lince/ClusterBytes/Student-Performance-Analysis/core/dataset_v2.csv')

# position=df.columns.get_loc(sys.argv[1])-1
col_name = df.columns[int(sys.argv[1])+1]
print(col_name)