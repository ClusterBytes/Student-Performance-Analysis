from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
print("The Dataset is \n",X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

print("The training set of X is\n",X_train)
print("The testing set of X is\n",X_test)

print("The training set of Y\n",y_train)
print("The testing set of Y\n",y_test)

log_reg = LogisticRegression()

log_reg.fit(X_train, y_train)

pred = log_reg.predict(X_test)
print("The predicted Y\n",pred)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, pred)
print("The accuracy is ",accuracy)