import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,precision_score, ConfusionMatrixDisplay
import os
from warnings import filterwarnings
filterwarnings('ignore')

data = pd.read_csv('/home/lince/ClusterBytes/Student-Performance-Analysis/core/result.csv', index_col=0)
orginal = pd.read_csv('/home/lince/ClusterBytes/Student-Performance-Analysis/core/dataset_v2.csv', index_col=0)

g = data.columns.get_loc('G1')
x = data.iloc[:,0:g] #features

y = data.loc[:,'G1':'G42'] #labels
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=48)

print("Splitting of x :\n", x_train.shape, x_test.shape)
print("Splitting of y:\n",y_train.shape, y_test.shape)

grade = []
accuracy = []
sub_list=[]
precision=[]
total_acc = 0
total_pre=0
col_names = orginal.iloc[:, 1:43].columns.tolist()

for i,sub in enumerate(col_names) :
    
    ind = 'G'+str(i+1)
    grade.append(ind)
    sub_list.append(sub)
    
    log_reg = LogisticRegression()

    model = OneVsRestClassifier(log_reg) #multiclass classification

    model.fit(x_train, y_train.loc[:,ind])
    y_pred = model.predict(x_test)
    # print(y_test.loc[:,ind]) #select only the specific column
    acc = accuracy_score(y_test.loc[:,ind], y_pred)
    prec=precision_score(y_test.loc[:,ind], y_pred,average="weighted")
    print('The Accuracy of',sub,'is',acc)
    print('The precision of ',sub,'is',prec)
    total_acc = total_acc + acc
    total_pre=total_pre+prec
    accuracy.append(acc)
    precision.append(prec)


    cm = confusion_matrix(y_test.loc[:, ind], y_pred, labels = model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)

    fig, ax = plt.subplots(figsize=(8, 8))
    disp.plot(ax=ax)
    ax.set_title(sub+" "+str(round(acc*100,2))+"%")
  
    plt.savefig(os.path.join('/home/lince/ClusterBytes/Student-Performance-Analysis/plot-for-LR', sub + '.png'))
    plt.close()
   


print("The average accuracy is",total_acc/42)   
print("The average precision is",total_pre/42)
# print(accuracy)
# print(precision)
u = sub_list[0:]
v = accuracy[0:]

plt.figure(figsize=(10,6))
plt.plot(u,v, scaley=False)
plt.xlabel('Subject')
plt.xticks(rotation=90)
plt.ylabel('Accuracy')
plt.title('Logistic Regression - Accuracy Graph')

plt.show()

u = sub_list[0:]
v = precision[0:]

plt.figure(figsize=(10,6))
plt.plot(u,v, scaley=False)
plt.xlabel('Subject')
plt.xticks(rotation=90)
plt.ylabel('Precision')
plt.title('Logistic Regression - Precision Graph')

plt.show()



