import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Datasets/new_data.csv', index_col = 0)

x = data.loc[:,'A1':'I42']
y = data.loc[:,'G1':'G42']

print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

total_acc = 0
for i in range(42):

    ind = 'G'+str(i+1)

    dt = DecisionTreeClassifier()
    dt.fit(x_train, y_train.loc[:,ind])
    
    y_pred = dt.predict(x_test)

    acc = accuracy_score(y_test.loc[:,ind], y_pred)
    print('The Accuracy of',ind,'is',acc)
    total_acc+=acc

print('The average accuracy is',total_acc/42)
