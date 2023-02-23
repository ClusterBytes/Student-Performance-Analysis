from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from .data import x_test, y_test, x_train, y_train

model = LogisticRegression(solver="newton-cg", max_iter=150)
model.fit(x_train, y_train)
pred2 = model.predict(x_test)
accuracy = accuracy_score(y_test, pred2)
print(accuracy)
