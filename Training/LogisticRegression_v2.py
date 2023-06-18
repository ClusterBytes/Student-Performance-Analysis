import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,ConfusionMatrixDisplay,f1_score
from sklearn.preprocessing import StandardScaler

data=pd.read_csv("../Dataset/CSV-Train/5_2_binned.csv",index_col=0)
X=data.iloc[:,:32]
y=data.iloc[:,32:]
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)

ss=StandardScaler(with_mean=True,with_std=True)
X_train_norm=ss.fit_transform(X_train)
X_test_norm=ss.transform(X_test)

accuracy={}
for c in y.columns:
    print('\n=========  Training :',c,' =========')
    lr=LogisticRegression(random_state=0,warm_start=True,max_iter=1000,solver='saga')
    lr.fit(X_train_norm,y_train[c])
    y_pred=lr.predict(X_train_norm)
    
    acc=accuracy_score(y_train[c],y_pred)
    pre=precision_score(y_train[c],y_pred,average='weighted',zero_division=1)
    rec=recall_score(y_train[c],y_pred,average='weighted')
    f1=f1_score(y_train[c],y_pred,average='weighted')
    
    cm=confusion_matrix(y_train[c],y_pred,labels=lr.classes_)
    print(cm)
    ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=lr.classes_).plot()
    # accuracy[c]=acc
    print('Accuracy =',acc)
    print('Precision =',pre)
    print('Recall =',rec)
    print('F1 score =',f1)

# for i in accuracy:
    # print(i,':',accuracy[i])
