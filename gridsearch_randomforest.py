
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from warnings import filterwarnings

filterwarnings("ignore")
# Load the dataset from a CSV file
data = pd.read_csv('result.csv', index_col='Reg_No')

g = data.columns.get_loc('G1')
k = data.columns.get_loc('G18')
X = data.iloc[:,0:g]
y = data.loc[:, 'G1':'G18']


models = {
    'Random Forest': RandomForestClassifier(random_state=0),
    }

# params = {
#        'Random Forest': {'n_estimators': [10, 50, 100, 150, 200],
#                      'max_depth': [None, 5, 10, 15, 20],
#                      'min_samples_split': [2, 5, 10],
#                      'min_samples_leaf': [1, 2, 4],
#                         }

# }

# params = {
#     'Random Forest': {
#         'n_estimators': [10, 50, 100, 150, 200],
#         'max_depth': [None, 5, 10, 20],
#         'min_samples_split': [2, 5, 10],
#         'min_samples_leaf': [1, 2, 4],
#         'max_features': ['sqrt', 'log2'],
#         'bootstrap': [True, False],
#         'class_weight': ['balanced', None],
#         'criterion': ['gini', 'entropy'],
#         'random_state': [0]
#     }
# }

params = {
    'Random Forest': {
        'n_estimators': [10, 50, 100,150],
        'max_features': ['sqrt', 'log2'],
        'max_depth': [10, 20, 30, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
}

grade = []
accuracy = []

# Perform grid search for each model
for i in range(18):
    ind = 'G' + str(i+1)
    grade.append(ind)
    for name, model in models.items():
        clf = GridSearchCV(model, params[name], cv=4, n_jobs=-1)
        # clf.fit(X, y)
        clf.fit(X, y.loc[:, ind])
        
        print(f'{name} Best Score: {clf.best_score_} Best Params: {clf.best_params_} of {ind}')
        accuracy.append(clf.best_score_)

u = grade[0:]
v = accuracy[0:]

plt.plot(u,v, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy')
plt.title('Random Forest')

plt.show()
