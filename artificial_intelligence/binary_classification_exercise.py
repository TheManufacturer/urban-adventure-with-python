# Use this code on colab Space - Google Research [colab.research.google.com]
# Without Comment
# If u want to use this in a space like [pycharm] u will install pandas/numpy/scikit-learn
# pip install (insert library)

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("https://proai-datasets.s3.eu-west-3.amazonaws.com/sample_dataset.csv")

X = df.drop('target', axis=1).select_dtypes(exclude='object')
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

cleaner = SimpleImputer()

cleaner.fit(X_train)

X_train = cleaner.transform(X_train)
X_test = cleaner.transform(X_test)

scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy_score(y_test, y_pred)

X = df.drop('target', axis=1).select_dtypes(exclude='object').iloc[:, 5]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

cleaner.fit(X_train)

X_train = cleaner.transform(X_train)
X_test = cleaner.transform(X_test)

scaler.fit(X_train)

X_train = cleaner.transform(X_train)
X_test = cleaner.transform(X_test)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy_score(y_test, y_pred)


