import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from warnings import filterwarnings
filterwarnings('ignore')


data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Data preprocessing/result.csv', index_col=0)

g = data.columns.get_loc('G1')
x = data.iloc[:,0:g]
y = data.loc[:,'G1':'G18']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

params = {
            'penalty':['l1', 'l2'],
            'C' : [0.1, 1.0, 2.0]
}

score = []
para = []
for i in range(18):
    
    ind = 'G'+str(i+1)
    
    log_reg = LogisticRegression()

    grid_sch = GridSearchCV(log_reg, param_grid=params, cv=5)

    grid_sch.fit(x_train, y_train.loc[:,ind])

    best_para = grid_sch.best_params_
    best_score = grid_sch.best_score_

    para.append(best_para)
    score.append(best_score)

    print('Best parameter of',ind,'is',grid_sch.best_params_)
    print('Best Score of',ind,'is',grid_sch.best_score_)


