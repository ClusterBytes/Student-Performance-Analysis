import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,precision_score, ConfusionMatrixDisplay
#import json
from warnings import filterwarnings
filterwarnings('ignore')

data = pd.read_csv('/home/lince/ClusterBytes/Student-Performance-Analysis/Data preprocessing/result.csv', index_col=0)
orginal = pd.read_csv('/home/lince/ClusterBytes/Student-Performance-Analysis/core/dataset_v2.csv', index_col=0)
print(data)
g = data.columns.get_loc('G1')
print(g)
x = data.iloc[:,0:g]
print(x)
y = data.loc[:,'G1':'G42']
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=48)

print("Splitting of x :\n", x_train.shape, x_test.shape)
print("Splitting of y:\n",y_train.shape, y_test.shape)

# with open('logistic_regression_para.json', 'r') as fp:
#     js = json.load(fp)

# C = js['C_para']
# penalty = js['penalty_para']
 
#reg = []
grade = []
accuracy = []
total_acc = 0
col_names = orginal.iloc[:, 1:43].columns.tolist()
# print(col_names)
for i,sub in enumerate(col_names) :
    
    ind = 'G'+str(i+1)
    grade.append(ind)
    
    model = LogisticRegression(warm_start=True)

    # model = OneVsRestClassifier(log_reg)

    model.fit(x_train, y_train.loc[:,ind])

    y_pred = model.predict(x_test)

    #reg.append(log_reg)
    
    acc = accuracy_score(y_test.loc[:,ind], y_pred)
    prec=precision_score(y_test.loc[:,ind], y_pred,average="weighted")
    print('The Accuracy of',sub,'is',acc)
    print('The precision of ',sub,'is',prec)
    total_acc = total_acc + acc
    accuracy.append(acc)

    cm = confusion_matrix(y_test.loc[:, ind], y_pred, labels = model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)

    # fig, ax = plt.subplots(figsize=(8, 8))
    # disp.plot(ax=ax)
    # ax.set_title(sub+" "+str(round(acc*100,2))+"%")
    # plt.show()


print("The average accuracy is",total_acc/42)    
u = grade[0:]
v = accuracy[0:]

plt.figure(figsize=(10,6))
plt.plot(u,v, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy')
plt.title('Logistic Regression')

plt.show()



