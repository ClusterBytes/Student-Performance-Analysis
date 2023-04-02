
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from warnings import filterwarnings

filterwarnings("ignore")
# Load the dataset from a CSV file
data = pd.read_csv('result.csv', index_col='Reg_No')

# Split the dataset into features and target
g = data.columns.get_loc('G1')
k = data.columns.get_loc('G18')
X = data.iloc[:,0:g]
# y = data['G1']
y = data.loc[:, 'G1':'G18']


# Define the models to be tested
models = {
    'SVM': SVC(random_state=0),
    }

# Define the hyperparameters to be tested for each model
params = {
    'SVM': {'C': [0.01, 0.1, 1, 10], 'kernel': ['linear', 'rbf'], 'gamma': ['scale', 'auto']}

}

grade = []
accuracy = []

# Perform grid search for each model
for i in range(18):
    ind = 'G' + str(i+1)
    grade.append(ind)
    for name, model in models.items():
        clf = GridSearchCV(model, params[name], cv=4)
        # clf.fit(X, y)
        clf.fit(X, y.loc[:, ind])
        
        print(f'{name} Best Score: {clf.best_score_} Best Params: {clf.best_params_} of {ind}')
        accuracy.append(clf.best_score_)

u = grade[0:]
v = accuracy[0:]

plt.plot(u,v, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy')
plt.title('SVM')

plt.show()
