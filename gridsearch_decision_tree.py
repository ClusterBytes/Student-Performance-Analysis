
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
# import json
import numpy
from warnings import filterwarnings


filterwarnings("ignore")
# Load the dataset from a CSV file
data = pd.read_csv('result.csv', index_col='Reg_No')

g = data.columns.get_loc('G1')
k = data.columns.get_loc('G42')
X = data.iloc[:,0:g]
y = data.loc[:, 'G1':'G42']


models = {
    'Decision Tree': DecisionTreeClassifier(random_state=0),
    }

params = {
    'Decision Tree': {
    'max_depth': [2, 4, 6, 8],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': [None, 'sqrt', 'log2']
    }

}

grade = []
accuracy = []

# max_depth_set = []
# min_samples_split_set = []
# min_samples_leaf_set = []
# max_features = []

# Perform grid search for each model
for i in range(42):
    ind = 'G' + str(i+1)
    grade.append(ind)
    for name, model in models.items():
        clf = GridSearchCV(model, params[name], cv=4)
        # clf.fit(X, y)
        clf.fit(X, y.loc[:, ind])
        
        print(f'{name} Best Score: {clf.best_score_} Best Params: {clf.best_params_} of {ind}')
        accuracy.append(clf.best_score_)


avg = numpy.average(accuracy)
print(f"Average accuracy = {avg}")
u = grade[0:]
v = accuracy[0:]

plt.plot(u,v, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy')
plt.title('Decision Tree')

plt.show()