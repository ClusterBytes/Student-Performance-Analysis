import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score
import os


data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Datasets/new_data.csv', index_col = 0)

# new_data = data[['A1','I1','G1']]
# print(new_data)



# x = new_data[['A1','I1']]
# y = new_data[['G1']]

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

# dt = DecisionTreeClassifier()
# dt.fit(x_train,y_test)

# y_pred = dt.predict(x_test)

# acc = accuracy_score(y_test,y_pred)

# print('The accuracy is',acc)

def run_single_subject():
    sub = input("Enter the subject to predict the grade:")
    columns_to_keep = ['A'+sub, 'I'+sub, 'G'+sub]
    new_data = data[columns_to_keep]
    new_data.to_csv('sub'+sub+'.csv')

    data1 = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/model_training/decision_tree/sub'+sub+'.csv', index_col = 0)

    x = data1.loc[:,'A'+sub : 'I'+sub]
    y = data1.loc[:,'G'+sub]

    print(x)
    print(y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

    dt = DecisionTreeClassifier()
    dt.fit(x_train,y_train)

    y_pred = dt.predict(x_test)

    acc = accuracy_score(y_test,y_pred)
    pre = precision_score(y_test,y_pred,average='weighted')

    print('The accuracy of G'+sub,'is',acc)
    print('The precision of G'+sub,'is',pre)

    os.remove('sub'+sub+'.csv')

ch = 'y'
while(ch != 'n'):
    run_single_subject()
    print('Do you want to continue(Enter y/n):')
    ch = input()

