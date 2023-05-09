import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB, GaussianNB, ComplementNB, BernoulliNB, CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score
from warnings import filterwarnings
filterwarnings('ignore')

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Datasets/new_data.csv', index_col=0)

print(data)

# g = data.columns.get_loc('G1')
x = data.loc[:,'A1':'I42']
y = data.loc[:,'G1':'G42']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

print("Splitting of x :\n", x_train.shape, x_test.shape)
print("Splitting of y:\n",y_train.shape, y_test.shape)
 

grade = []
accuracy = []
precision = []

total_acc = 0
total_pre = 0
for i in range(42):
    
    ind = 'G'+str(i+1)
    grade.append(ind)
    
    gnb = GaussianNB()

    gnb.fit(x_train, y_train.loc[:,ind])
    
    y_pred = gnb.predict(x_test)
    
    acc = accuracy_score(y_test.loc[:,ind], y_pred)
    print('The Accuracy of',ind,'is',acc)

    pre = precision_score(y_test.loc[:,ind], y_pred, average='weighted')
    print('The precision of',ind,'is',pre)
    
    total_acc += acc
    total_pre += pre

    accuracy.append(acc)
    precision.append(pre)

    cm = confusion_matrix(y_test.loc[:, ind], y_pred, labels = gnb.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=gnb.classes_)


    disp.plot()
    disp.figure_.savefig('D:/Main_Project/Student-Performance-Analysis/model_training/naive_bayes/NB_images/'+ind+'.png')

print("Average accuracy is",total_acc/42)   
print("Average precision is",total_pre/42)   
u = grade[0:]
v = accuracy[0:]
w = precision[0:]
plt.figure(figsize=(10,6))
plt.plot(u,v,w,scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy and Precision')
plt.title('Naive Bayes')
plt.legend(['Accuracy', 'Precision'], loc = 'lower right')

plt.show()