from sklearn.datasets import make_regression

x, y = make_regression(n_samples=100, n_features=1, n_targets=1)

print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(x)