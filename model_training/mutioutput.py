import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score

from warnings import filterwarnings
filterwarnings('ignore')

data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Data preprocessing/result.csv', index_col=0)

g = data.columns.get_loc('G1')
x = data.iloc[:,0:g]
y = data.loc[:,'G1':'G18']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

log = LogisticRegression()

clf = MultiOutputClassifier(log)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print(y_pred.shape)
#acc = accuracy_score(y_test, y_pred)
# print('The accuracy is',clf.score(y_test, y_pred))