import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Data preprocessing/result.csv', index_col=0)
print(data)

g = data.columns.get_loc('G1')
k = data.columns.get_loc('G18')
x = data.iloc[:,0:g]
#y = data['G18']
y = data.loc[:,'G1':'G18']
print("Training set:\n",x)
print("Testing set:\n",y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

print("Splitting of x :\n", x_train.shape, x_test.shape)
print("Splitting of y:\n",y_train.shape, y_test.shape)
 
reg = []
grade = []
accuracy = []
for i in range(18):
    
    ind = 'G'+str(i+1)
    grade.append(ind)
    
    log_reg = LogisticRegression()

    log_reg.fit(x_train, y_train.loc[:,ind])

    y_pred = log_reg.predict(x_test)

    reg.append(log_reg)
    
    acc = accuracy_score(y_test.loc[:,ind], y_pred)
    accuracy.append(acc)
    
for i in range(len(accuracy)):
    g = 'G'+str(i+1)
    print("The accuracy of",g,"is",accuracy[i])

u = grade[0:]
v = accuracy[0:]

plt.plot(u,v, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy')
plt.title('Logistic Regression')

plt.show()