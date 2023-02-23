from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from data import x_test, y_test, x_train, y_train

model = LogisticRegression(solver="newton-cg", max_iter=150)  # load algorithm
model.fit(x_train, y_train)  # train using lr
pred2 = model.predict(x_test)
print(x_test)
print(pred2)
# print(y_test)
accuracy = accuracy_score(y_test, pred2)
print(accuracy)
