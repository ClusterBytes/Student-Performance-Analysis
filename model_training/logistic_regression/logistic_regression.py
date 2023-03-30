import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
import json
from warnings import filterwarnings
filterwarnings('ignore')

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Data preprocessing/result.csv', index_col=0)

g = data.columns.get_loc('G1')
x = data.iloc[:,0:g]
y = data.loc[:,'G1':'G18']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

print("Splitting of x :\n", x_train.shape, x_test.shape)
print("Splitting of y:\n",y_train.shape, y_test.shape)

with open('logistic_regression_para.json', 'r') as fp:
    js = json.load(fp)

C = js['C_para']
penalty = js['penalty_para']
 
reg = []
grade = []
accuracy = []
total_acc = 0
for i in range(18):
    
    ind = 'G'+str(i+1)
    grade.append(ind)
    
    log_reg = LogisticRegression(penalty=penalty[i], C=C[i])

    log_reg.fit(x_train, y_train.loc[:,ind])

    y_pred = log_reg.predict(x_test)

    reg.append(log_reg)
    
    acc = accuracy_score(y_test.loc[:,ind], y_pred)
    print('The Accuracy of',ind,'is',acc)
    total_acc = total_acc + acc
    accuracy.append(acc)


print("The average accuracy is",total_acc/18)    
u = grade[0:]
v = accuracy[0:]

plt.figure(figsize=(10,6))
plt.plot(u,v, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy')
plt.title('Logistic Regression')

plt.show()