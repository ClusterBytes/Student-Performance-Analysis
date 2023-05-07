import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix,precision_score, ConfusionMatrixDisplay
from warnings import filterwarnings

filterwarnings('ignore')

data = pd.read_csv('result.csv', index_col=0)

g = data.columns.get_loc('G1')
x = data.iloc[:,0:g]
y = data.loc[:,'G1':'G42']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=48)

models = {
    'SVM': SVC(random_state=0),
}

params = {
    'SVM': {'C': [0.01, 0.1, 1, 10], 'kernel': ['linear', 'rbf'], 'gamma': ['scale', 'auto']}
}

grade = []
accuracy = []
precision = []
total_acc = 0
col_names = y.columns.tolist()

if not os.path.exists('plots'):
    os.mkdir('plots')

for i, sub in enumerate(col_names):
    
    ind = 'G'+str(i+1)
    grade.append(ind)
    
    clf = GridSearchCV(models['SVM'], params['SVM'], cv=4)
    clf.fit(x_train, y_train.loc[:,ind])

    y_pred = clf.predict(x_test)
    
    acc = accuracy_score(y_test.loc[:,ind], y_pred)
    prec=precision_score(y_test.loc[:,ind], y_pred,average="weighted")
    print('The Accuracy of',sub,'is',acc)
    print('The precision of ',sub,'is',prec)
    total_acc = total_acc + acc
    accuracy.append(acc)
    precision.append(prec)

    cm = confusion_matrix(y_test.loc[:, ind], y_pred, labels = clf.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)

    fig, ax = plt.subplots(figsize=(8, 8))
    disp.plot(ax=ax)
    ax.set_title(sub+" "+str(round(acc*100,2))+"%")
    plt.savefig(os.path.join('plots/', sub + '.png'))
    plt.close()



