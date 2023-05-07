import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, ConfusionMatrixDisplay
from warnings import filterwarnings

filterwarnings('ignore')

data = pd.read_csv('result.csv', index_col=0)

g = data.columns.get_loc('G1')
x = data.iloc[:, 0:g]
y = data.loc[:, 'G1':'G42']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=48)

models = {
    'RF': RandomForestClassifier(random_state=0),
}

params = {
    'RF': {'n_estimators': [100, 200, 300], 'max_depth': [5, 10, 20]}
}

if not os.path.exists('plots for RF'):
    os.mkdir('plots for RF')

grade = []
accuracy = []
precision = []
total_acc = 0
col_names = y.columns.tolist()

for i, sub in enumerate(col_names):

    ind = 'G' + str(i + 1)
    grade.append(ind)

    clf = GridSearchCV(models['RF'], params['RF'], cv=4)
    clf.fit(x_train, y_train.loc[:, ind])

    y_pred = clf.predict(x_test)

    acc = accuracy_score(y_test.loc[:, ind], y_pred)
    prec = precision_score(y_test.loc[:, ind], y_pred, average="weighted")
    print('The Accuracy of', sub, 'is', acc)
    print('The precision of ', sub, 'is', prec)
    total_acc = total_acc + acc
    accuracy.append(acc)
    precision.append(prec)

    cm = confusion_matrix(y_test.loc[:, ind], y_pred, labels=clf.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)

    fig, ax = plt.subplots(figsize=(8, 8))
    disp.plot(ax=ax)
    ax.set_title(sub + " " + str(round(acc * 100, 2)) + "%")
    plt.savefig(os.path.join('plots for RF/', sub + '.png'))
    plt.close()

print(accuracy)
print(precision)
avg = numpy.average(accuracy)
print(f"Average accuracy = {avg}")
avg1 = numpy.average(precision)
print(f"Average accuracy = {avg1}")
