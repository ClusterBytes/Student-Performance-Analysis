import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('../Dataset/CSV-Single/6_sgpa1_sgpa2.csv',index_col='Reg_No')

print('\n____description____')
print(data.describe())

print('\n____covarience____')
print(data.cov())

print('\n____correlation____')
print(data.corr())


plt.scatter(data.iloc[:,0],data.iloc[:,1])
plt.show()