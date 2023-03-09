import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Data preprocessing/result.csv', index_col=0)
print(data)

g = data.columns.get_loc('G1')
k = data.columns.get_loc('G18')
x = data.iloc[:,0:g]
y = data['G18']

print("Training set:\n",x)
print("Testing set:\n",y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

print("Splitting of x :\n", x_train.shape, x_test.shape)
print("Splitting of y:\n",y_train.shape, y_test.shape)

    

log_reg = LogisticRegression()

log_reg.fit(x_train, y_train)

y_pred = log_reg.predict(x_test)

print("y_test", y_test)


print(y_pred)

acc = accuracy_score(y_test, y_pred)
print("Accuracy:",acc)
