import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm

from sklearn import datasets

data = pd.read_csv("result.csv", index_col="Reg_No")
# print(data.dtypes)
iris = datasets.load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target

# Save the DataFrame as a CSV file
iris_df.to_csv("iris.csv", index=False)
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=0)
clf = svm.SVC(kernel="linear", C=1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(y_test)
print(y_pred)

from sklearn.metrics import accuracy_score

print("Accuracy:", accuracy_score(y_test, y_pred))
