import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from warnings import filterwarnings

filterwarnings("ignore")
# Load the dataset from a CSV file
data = pd.read_csv('result.csv', index_col='Reg_No')

g = data.columns.get_loc('G1')
k = data.columns.get_loc('G42')
X = data.iloc[:,0:g]
y = data.loc[:, 'G1':'G42']


models = {
    'Random Forest': RandomForestClassifier(random_state=0),
    }


params = {
    'Random Forest': {
        'n_estimators': [10, 50, 100,150],
        'max_features': ['sqrt', 'log2'],
        'max_depth': [10, 20, 30, None],
        
    }
}

grade = []
accuracy = []

# Perform grid search for each model
for i in range(42):
    ind = 'G' + str(i+1)
    grade.append(ind)
    for name, model in models.items():
        clf = GridSearchCV(model, params[name], cv=4, n_jobs=-1)
        # clf.fit(X, y)
        clf.fit(X, y.loc[:, ind])
        
        print(f'{name} Best Score: {clf.best_score_} Best Params: {clf.best_params_} of {ind}')
        accuracy.append(clf.best_score_)

avg = numpy.average(accuracy)
print(f"Average accuracy = {avg}")
u = grade[0:]
v = accuracy[0:]
print(accuracy)
plt.plot(u,v, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy')
plt.title('Random Forest')

plt.show()
