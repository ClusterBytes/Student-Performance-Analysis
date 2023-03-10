
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron

# Load the dataset from a CSV file
data = pd.read_csv('result.csv', index_col='Reg_No')

# Split the dataset into features and target
X = data.drop('G1',axis=1)
# y = data['G1']
y = data.loc[:, 'G1':'G18']


# Define the models to be tested
models = {
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC(),
    'Perceptron': Perceptron()
}

# Define the hyperparameters to be tested for each model
params = {
    'Decision Tree': {'max_depth': [2, 4, 6, 8]},
    'Random Forest': {'n_estimators': [10, 50, 100, 200]},
    'SVM': {'C': [0.1, 1, 10, 100]},
    'Perceptron': {'alpha': [0.0001, 0.001, 0.01, 0.1]}
}


# Perform grid search for each model
for i in range(18):
    ind = 'G' + str(i+1)
    for name, model in models.items():
        clf = GridSearchCV(model, params[name], cv=4)
        # clf.fit(X, y)
        clf.fit(X, y.loc[:, ind])
        
        print(f'{name} Best Score: {clf.best_score_} Best Params: {clf.best_params_} of {ind}')
