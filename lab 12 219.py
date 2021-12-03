# -*- coding: utf-8 -*-
"""


Created on Sat Nov 27 22:53:12 2021

@author: RANA
"""
import pandas as pd
df = pd.read_csv('data.csv')

df.describe().transpose()

X = df.drop('Facies',axis=1)
y = df['Facies']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Fit only to the training data
scaler.fit(X_train)

StandardScaler(copy=True, with_mean=True, with_std=True)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(4,4,4),max_iter=1000)
mlp.fit(X_train,y_train)
predictions = mlp.predict(X_test)
from sklearn.metrics import classification_report

print(classification_report(y_test,predictions))
