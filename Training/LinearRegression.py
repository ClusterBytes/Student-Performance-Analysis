from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

data=pd.read_csv('../Dataset/CSV-Single/6_sgpa1_sgpa2.csv',index_col='Reg_No')
x=data.iloc[:,0].values.reshape(-1,1)
y=data.iloc[:,1].values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

model = LinearRegression()

print('...Started training...')
model.fit(x_train, y_train)
print('...Completed training...\nStarted predicting...')
y_pred = model.predict(x_test)

error = mean_squared_error(y_test, y_pred)
print(error)