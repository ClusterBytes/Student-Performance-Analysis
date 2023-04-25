import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,precision_score, ConfusionMatrixDisplay
#import json
from warnings import filterwarnings
filterwarnings('ignore')

data = pd.read_csv('/home/lince/ClusterBytes/Student-Performance-Analysis/Data preprocessing/HUN102_encode.csv', index_col=0)



x = data.iloc[:,0:2]

# print(data.index)
y = data.loc[:,'G31']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=48)
print("Splitting of x :\n", x_train.shape, x_test.shape)
print("Splitting of y:\n",y_train.shape, y_test.shape)
model = LogisticRegression(warm_start=True)
# model = OneVsRestClassifier(log_reg)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
    #reg.append(log_reg)

df = pd.DataFrame({'Reg_No':y_test.index.values,'actual': y_test.values, 'predicted': y_pred})
def decode_value(val):
    if val == 9:
        return 'S'
    elif val == 8:
        return 'A+'
    elif val == 7:
        return 'A'
    elif val == 6:
        return 'B+'
    elif val == 5:
        return 'B'
    elif val == 4:
        return 'C+'
    elif val == 3:
        return 'C'
    elif val == 2:
        return 'D'
    elif val == 1:
        return 'P'
    else:
        return 'F'
df['actual_grade'] = df['actual'].apply(lambda x: decode_value(x))
df['predicted_grade'] = df['predicted'].apply(lambda x: decode_value(x))
df.to_csv('HUN102_a_p_mod.csv', index=False)
acc = accuracy_score(y_test, y_pred)
prec=precision_score(y_test, y_pred,average="weighted")
print('The Accuracy of HUN102 is',acc)
print('The precision of  HUN102 is',prec)


