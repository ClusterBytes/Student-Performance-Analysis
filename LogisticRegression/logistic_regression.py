import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer


def sklearn_to_df(data_loader):
    X_data = data_loader.data
    X_columns = data_loader.feature_names
    x = pd.DataFrame(X_data, columns=X_columns)
    print(x)


sklearn_to_df(load_breast_cancer())
