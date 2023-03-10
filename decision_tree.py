# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import f1_score, precision_score, recall_score

# #  Read CSV file into a pandas DataFrame with the first column as index
# data = pd.read_csv('result.csv', index_col='Reg_No')

# # Preprocess data as needed (e.g., remove missing values, convert categorical variables, etc.)

# # Split data into training and testing sets
# X = data.drop(columns=['G3'])
# y = data['G3']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Create decision tree classifier object
# clf = DecisionTreeClassifier()

# # Train the classifier on the training data
# clf.fit(X_train, y_train)

# # Predict the target variable on the testing data
# y_pred = clf.predict(X_test)

# # Evaluate the performance of the classifier
# accuracy = clf.score(X_test, y_test)
# print("Accuracy:", accuracy)

# f1 = f1_score(y_test, y_pred, average='micro')
# precision = precision_score(y_test, y_pred, average='micro')
# recall = recall_score(y_test, y_pred, average='micro')

# print("F1-score:", f1)
# print("Precision:", precision)
# print("Recall:", recall)



# import pandas as pd
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import make_scorer, f1_score

# # Load the CSV file into a pandas DataFrame
# df = pd.read_csv('result.csv')

# # Split the dataset into features (X) and target variable (y)
# X = df.drop('Grade__G1', axis=1)
# y = df['Grade__G1']

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Define the hyperparameters and their ranges for grid search
# param_grid = {
#     'max_depth': [5, 10, 15, 20],
#     'min_samples_split': [2, 5, 10, 20],
#     'min_samples_leaf': [1, 2, 4, 8],
#     'criterion': ['gini', 'entropy']
# }

# # Create a decision tree classifier object
# clf = DecisionTreeClassifier()

# # Define the scoring metric (F1 score)
# scorer = make_scorer(f1_score, average='micro')

# # Create a GridSearchCV object
# grid_obj = GridSearchCV(clf, param_grid, scoring=scorer,cv=4)

# # Fit the GridSearchCV object to the training data
# grid_fit = grid_obj.fit(X_train, y_train)

# # Get the best hyperparameters
# best_clf = grid_fit.best_estimator_
# print(best_clf)

# # Use the best model to predict the target variable on the testing data
# y_pred = best_clf.predict(X_test)

# # Evaluate the performance of the model using F1 score
# f1 = f1_score(y_test, y_pred, average='micro')
# print("F1-score:", f1)


import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron

# Load the dataset from a CSV file
data = pd.read_csv('result.csv', index_col='Reg_No')

# Split the dataset into features and target
X = data.drop('G1', axis=1)
y = data['G1']

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
for name, model in models.items():
    clf = GridSearchCV(model, params[name], cv=4)
    clf.fit(X, y)
    print(f'{name} Best Score: {clf.best_score_} Best Params: {clf.best_params_}')
