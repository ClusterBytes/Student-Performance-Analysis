import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB, GaussianNB, ComplementNB, BernoulliNB, CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score
from warnings import filterwarnings
filterwarnings('ignore')

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Data preprocessing/result.csv', index_col=0)

g = data.columns.get_loc('G1')
x = data.iloc[:,0:g]
y = data.loc[:,'G1':'G18']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

print("Splitting of x :\n", x_train.shape, x_test.shape)
print("Splitting of y:\n",y_train.shape, y_test.shape)
 
gnb_set = []
grade = []
accuracy = []

total_acc = 0
for i in range(18):
    
    ind = 'G'+str(i+1)
    grade.append(ind)
    
    gnb = ComplementNB()

    gnb.fit(x_train, y_train.loc[:,ind])
    
    y_pred = gnb.predict(x_test)

    gnb_set.append(gnb)
    
    acc = accuracy_score(y_test.loc[:,ind], y_pred)
    print('The Accuracy of',ind,'is',acc)
    
    total_acc = total_acc + acc

    accuracy.append(acc)


print("Average accuracy is",total_acc/18)   
u = grade[0:]
v = accuracy[0:]

plt.figure(figsize=(10,6))
plt.plot(u,v, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy')
plt.title('Naive Bayes')


plt.show()