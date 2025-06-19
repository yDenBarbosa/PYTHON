import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math as mt
from scipy.stats import mode
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report

# Split Data
df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula12/iris.csv')
X = df.drop(columns = 'Species')
Y = df['Species']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 10)

# Model

boost = XGBClassifier(n_estimators = 300, max_depth = 5)

boost.fit(X_train, Y_train)

Y_predict = boost.predict(X_test)

print(Y_test.tolist())
print(Y_predict)

print("Classification Report:\n", classification_report(Y_test, Y_predict))

scores = cross_val_score(boost, X, Y, cv=10)
print("Cross-Validation Accuracy Scores:", scores)
print("Mean Accuracy:", scores.mean())

#Cross checked accuracy: ~95.19%