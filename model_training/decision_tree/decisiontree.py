import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix, ConfusionMatrixDisplay
from warnings import filterwarnings
filterwarnings('ignore')

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Datasets/new_data.csv', index_col = 0)

x = data.loc[:,'A1':'I42']
y = data.loc[:,'G1':'G42']

print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

total_acc = 0
total_pre = 0
grade = []
accuracy = []
precision = []
for i in range(42):

    ind = 'G'+str(i+1)
    grade.append(ind)

    model = DecisionTreeClassifier()
    model.fit(x_train, y_train.loc[:,ind])
    
    y_pred = model.predict(x_test)

    acc = accuracy_score(y_test.loc[:,ind], y_pred)
    pre = precision_score(y_test.loc[:,ind], y_pred, average='weighted')
    print('The Accuracy of',ind,'is',acc)
    print('The precision of',ind,'is',pre)
    accuracy.append(acc)
    precision.append(pre)
    total_acc+=acc
    total_pre+=pre

    cm = confusion_matrix(y_test.loc[:, ind], y_pred, labels = model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)


    disp.plot()
    disp.figure_.savefig('D:/Main_Project/Student-Performance-Analysis/model_training/decision_tree/dt_images/'+ind+'.png')

print(precision)

print('The average accuracy is',total_acc/42)
print('The average precision is',total_pre/42)
u = grade[0:]
v = accuracy[0:]
w = precision[0:]
l = [v, w]
plt.figure(figsize=(10,6))
plt.plot(u, v, w, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy and precision')
plt.title('Decision Tree')
plt.legend(['accuracy','precision'], loc = 'lower right')

plt.show()
