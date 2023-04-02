import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
import json
from warnings import filterwarnings
filterwarnings('ignore')


data = pd.read_csv('D:/Main_Project/Student-Performance-Analysis/Data preprocessing/result.csv', index_col=0)

g = data.columns.get_loc('G1')
x = data.iloc[:,0:g]
y = data.loc[:,'G1':'G18']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

params = {
            'penalty':['l1', 'l2'],
            'C' : [0.1, 1.0]
}

# score = []
# para = []
score = []
grade = []
C_set = []
penalty_set = []
total = 0
for i in range(18):
    
    ind = 'G'+str(i+1)

    grade.append(ind)
    
    log_reg = LogisticRegression()

    grid_sch = GridSearchCV(log_reg, param_grid=params, cv=5)

    grid_sch.fit(x_train, y_train.loc[:,ind])

    best_para = grid_sch.best_params_
    best_score = grid_sch.best_score_

    score.append(best_score)
    total = total + best_score

    C_set.append(best_para['C'])
    penalty_set.append(best_para['penalty'])

    # para.append(best_para)
    # score.append(best_score)

    print('Best parameter of',ind,'is',grid_sch.best_params_)
    print('Best Score of',ind,'is',grid_sch.best_score_)

best_para = {
    'C_para': C_set,
    'penalty_para' : penalty_set,
    'score' : score
}

js = json.dumps(best_para, indent=3)

with open('logistic_regression_para.json', 'w') as fp:
    fp.write(js)

print("The average accuracy is",total/18)


u = grade[0:]
v = score[0:]

plt.figure(figsize=(10,6))
plt.plot(u,v, scaley=False)
plt.xlabel('Grade')
plt.ylabel('Accuracy')
plt.title('Logistic Regression')

plt.show()

