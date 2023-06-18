print('...Importing...')
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import pandas as pd
import matplotlib.pyplot as plt

print('...Reading...')
data=pd.read_csv('../Dataset/CSV-Single/6_sgpa1_sgpa2.csv',index_col='Reg_No')
x=data.iloc[:,0].values.reshape(-1,1)
y=data.iloc[:,1].values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

model = LinearRegression()

print('...Started training...')
model.fit(x_train, y_train)
print('...Completed training...\nStarted predicting...')
y_pred = model.predict(x_test)

rmse = mean_squared_error(y_test, y_pred,squared=False)
r2 = r2_score(y_test,y_pred)

print('Covariance =\n',data.cov())
print('Correlation =\n',data.corr())
print('RMSE =',rmse)
print('R2 =',r2)

plt.scatter(x_test, y_test, color='blue', label='Actual Data')
plt.plot(x_test, y_pred, color='red', label='Fitted Line')

plt.xlabel('SGPA_1')
plt.ylabel('SGPA_2')
plt.title('LinearRegression on v6')
plt.legend()
plt.show()




