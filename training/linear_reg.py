from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

x, y = make_regression(n_samples=100, n_features=1)

print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

model = LinearRegression()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print(y_test,"\n", y_pred)

error = mean_squared_error(y_test, y_pred)
print(error)