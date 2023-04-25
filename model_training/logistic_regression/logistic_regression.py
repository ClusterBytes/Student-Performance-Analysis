import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
#import json
from warnings import filterwarnings
filterwarnings('ignore')

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Datasets/new_data.csv', index_col=0)

#g = data.columns.get_loc('A18')
x = data.loc[:,'Dept_CSE':'I42']
y = data.loc[:,'G1':'G42']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

print("Splitting of x :\n", x_train.shape, x_test.shape)
print("Splitting of y:\n",y_train.shape, y_test.shape)

# with open('logistic_regression_para.json', 'r') as fp:
#     js = json.load(fp)

# C = js['C_para']
# penalty = js['penalty_para']
 
#reg = []
grade = []
accuracy = []
total_acc = 0
for i in range(42):
    
    ind = 'G'+str(i+1)
    grade.append(ind)
    
    log_reg = LogisticRegression()

    model = OneVsRestClassifier(log_reg)

    model.fit(x_train, y_train.loc[:,ind])

    y_pred = model.predict(x_test)

    #reg.append(log_reg)
    
    acc = accuracy_score(y_test.loc[:,ind], y_pred)
    print('The Accuracy of',ind,'is',acc)
    total_acc = total_acc + acc
    accuracy.append(acc)

    # cm = confusion_matrix(y_test.loc[:, ind], y_pred, labels = model.classes_)
    # disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)


    # disp.plot()


print("The average accuracy is",total_acc/42)    
u = grade[0:]
v = accuracy[0:]

plt.figure(figsize=(10,6))
plt.plot(u,v, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy')
plt.title('Logistic Regression')

plt.show()