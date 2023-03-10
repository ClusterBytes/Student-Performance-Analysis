# import pandas as pd
# from sklearn.svm import SVC
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.preprocessing import MultiLabelBinarizer

# # Load the CSV file using pandas
# df = pd.read_csv('result.csv',index_col="Reg_No")

# # Combine the values of multiple columns into a single string to use as the label
# df['labels'] = df[['G1','G2','G3','G4','G5','G6','G7']].apply(lambda x: ','.join(x.astype(str)), axis=1)


# # n_classes = len(df['labels'].unique())
# # if n_classes < 2:
# #     print("Error: The number of unique classes is less than 2.")
# #     exit()
    
# # Split the dataset into features (X) and labels (y)
# X = df.drop(['G1','G2','G3','G4','G5','G6','G7','labels'], axis=1) # replace 'label1', 'label2', 'label3', and 'labels' with the names of the columns
# y = df['labels']

# # Convert the labels into a binary matrix
# mlb = MultiLabelBinarizer()
# y = mlb.fit_transform(y)

# # Convert the binary matrix into a 1D array of labels
# y = y.argmax(axis=1)

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train the SVM model
# svm = SVC(kernel='linear')
# svm.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = svm.predict(X_test)

# # Evaluate the performance of the model
# print('Accuracy:', accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))



# import pandas as pd
# from sklearn.svm import SVC
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.preprocessing import LabelEncoder

# # Load the CSV file using pandas
# df = pd.read_csv('result.csv')

# # Check the number of unique classes in the label data
# # n_classes = len(df.filter(regex='^G_\d$').stack().unique())
# n_classes = len(df.filter(regex='^Grade__G\d$').stack().unique())
# print(n_classes)
# if n_classes < 2:
#     print("Error: The number of unique classes is less than 2.")
#     exit()

# # Combine the values of multiple columns into a single string to use as the label
# df['labels'] = df.filter(regex='^Grade__G\d$').apply(lambda x: ','.join(x.astype(str)), axis=1)

# # Convert the labels into numerical values
# le = LabelEncoder()
# y = le.fit_transform(df['labels'])

# # Split the dataset into features (X) and labels (y)
# X = df.drop(['Grade__G1','Grade__G2', 'labels'], axis=1) # replace 'G_1', 'G_2', 'G_3', and 'labels' with the names of the columns

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train the SVM model
# svm = SVC(kernel='linear')
# svm.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = svm.predict(X_test)

# # Convert the numerical labels back to the original labels
# y_test = le.inverse_transform(y_test)
# y_pred = le.inverse_transform(y_pred)

# # Evaluate the performance of the model
# print('Accuracy:', accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))


import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load the CSV file using pandas
df = pd.read_csv('result.csv',index_col="Reg_No")

# Combine the values of multiple columns into a single string to use as the label
df['labels'] = df.filter(regex='^G\d$').apply(lambda x: ','.join(x.astype(str)), axis=1)

# Check the number of unique classes in the label data
unique_labels = df['labels'].unique()
n_classes = len(unique_labels)
print('Unique Labels:', unique_labels)
print('Number of Unique Classes:', n_classes)
if n_classes < 2:
    print("Error: The number of unique classes is less than 2.")
    exit()

# Convert the labels into numerical values
le = LabelEncoder()
y = le.fit_transform(df['labels'])

# Split the dataset into features (X) and labels (y)
X = df.drop(['G1','G2', 'labels'], axis=1) # replace 'G_1', 'G_2', 'G_3', and 'labels' with the names of the columns

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the SVM model
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm.predict(X_test)

# Convert the numerical labels back to the original labels
y_test = le.inverse_transform(y_test)
y_pred = le.inverse_transform(y_pred)

# Evaluate the performance of the model
print('Accuracy:', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))



# import pandas as pd
# from sklearn.svm import SVC
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.preprocessing import LabelEncoder

# # Load the CSV file using pandas
# df = pd.read_csv('result.csv',index_col="Reg_No")

# # Check the number of unique classes in the label data
# n_classes = len(df.filter(regex='^G\d$').stack().unique())
# print(n_classes)
# if n_classes < 2:
#     print("Error: The number of unique classes is less than 2.")
#     exit()

# # Combine the values of multiple columns into a single string to use as the label
# df['labels'] = df.filter(regex='^G\d$').apply(lambda x: ','.join(x.astype(str)), axis=1)

# # Convert the labels into numerical values
# le = LabelEncoder()
# y = le.fit_transform(df['labels'])

# # Convert the binary matrix into a 1D array of labels
# # y = y.argmax(axis=1)

# # Split the dataset into features (X) and labels (y)
# X = df.drop(['G1', 'labels'], axis=1) # replace 'G_1', 'G_2', 'G_3', and 'labels' with the names of the columns

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train the SVM model
# svm = SVC(kernel='linear')
# svm.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = svm.predict(X_test)

# # Convert the numerical labels back to the original labels
# y_test = le.inverse_transform(y_test)
# y_pred = le.inverse_transform(y_pred)

# # Evaluate the performance of the model
# print('Accuracy:', accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))

