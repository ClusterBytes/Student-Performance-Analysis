import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, ConfusionMatrixDisplay
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# import json
from warnings import filterwarnings

filterwarnings("ignore")
import sys

subject = sys.argv[1]
data = pd.read_csv(subject + "_encode.csv", index_col=0)

x = data.iloc[:, 0:2]

y = data.loc[:, "G" + sys.argv[2]]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=48)
print("Splitting of x :\n", x_train.shape, x_test.shape)
print("Splitting of y:\n", y_train.shape, y_test.shape)


def actual_predicted(y_test, y_pred, subject):
    df = pd.DataFrame({"Reg_No": y_test.index.values, "actual": y_test.values, "predicted": y_pred})

    def decode_value(val):
        if val == 9:
            return "S"
        elif val == 8:
            return "A+"
        elif val == 7:
            return "A"
        elif val == 6:
            return "B+"
        elif val == 5:
            return "B"
        elif val == 4:
            return "C+"
        elif val == 3:
            return "C"
        elif val == 2:
            return "D"
        elif val == 1:
            return "P"
        else:
            return "F"

    df["actual_grade"] = df["actual"].apply(lambda x: decode_value(x))
    df["predicted_grade"] = df["predicted"].apply(lambda x: decode_value(x))
    df.to_csv("trained_" + subject + ".csv", index=False)

lda = LinearDiscriminantAnalysis()
lda.fit(x_train,y_train)
X_lda = lda.transform(x_train)
model = LogisticRegression(warm_start=True)
# model = OneVsRestClassifier(log_reg)
model.fit(x_train, y_train)
# model.fit(X_lda, y_train)

y_pred = model.predict(x_test)

print("____________________________________________")
print("using logistic regression")
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average="weighted")
print("The Accuracy of " + subject + " is", acc)
print("The precision of " + subject + " is", prec)
actual_predicted(y_test, y_pred, subject)


print("_____________________________________________")
print("using NaiveBayes")

from sklearn.naive_bayes import ComplementNB

gnb = ComplementNB()

gnb.fit(x_train, y_train)

y_pred_naive = gnb.predict(x_test)
acc = accuracy_score(y_test, y_pred_naive)
prec = precision_score(y_test, y_pred_naive, average="weighted")
print("The Accuracy of " + subject + " is", acc)
print("The precision of " + subject + " is", prec)

"""-----------------------------------------------------------------------"""
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=0),
    "Random Forest": RandomForestClassifier(random_state=0),
    "SVM": SVC(random_state=0),
    "Perceptron": Perceptron(),
}

# Define the hyperparameters to be tested for each model
params = {
    "Decision Tree": {"max_depth": [2, 4, 6, 8]},
    "Random Forest": {"n_estimators": [10, 50, 100, 200]},
    "SVM": {"C": [0.1, 1, 10, 100]},
    "Perceptron": {"alpha": [0.0001, 0.001, 0.01, 0.1]},
}
for name, model in models.items():
    clf = GridSearchCV(model, params[name], cv=4)
    # clf.fit(X, y)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("_______________________________________________")
    print("using " + name)
    prec = precision_score(y_test, y_pred, average="weighted")
    print("The Accuracy of " + subject + " is", acc)
    print("The precision of " + subject + " is", prec)
