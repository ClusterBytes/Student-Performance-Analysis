
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from warnings import filterwarnings

filterwarnings("ignore")
# Load the dataset from a CSV file
data = pd.read_csv('result.csv', index_col='Reg_No')

g = data.columns.get_loc('G1')
k = data.columns.get_loc('G18')
X = data.iloc[:,0:g]
y = data.loc[:, 'G1':'G18']


models = {
    'Decision Tree': DecisionTreeClassifier(random_state=0),
    }

params = {
    'Decision Tree': {'max_depth': [2, 4, 6, 8]},
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': [None, 'sqrt', 'log2']

}


# Perform grid search for each model
for i in range(18):
    ind = 'G' + str(i+1)
    for name, model in models.items():
        clf = GridSearchCV(model, params[name], cv=4)
        # clf.fit(X, y)
        clf.fit(X, y.loc[:, ind])
        
        print(f'{name} Best Score: {clf.best_score_} Best Params: {clf.best_params_} of {ind}')
