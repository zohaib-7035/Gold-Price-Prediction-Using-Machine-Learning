# -*- coding: utf-8 -*-
"""Gold Price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ggxZR_eJXkFDH3UZV0jHnRzd10yswake
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

data=pd.read_csv('data.csv')

data.head()

data.tail()

data.shape

data.info()

data.isnull().sum()

data.describe()

correlation = data.corr(numeric_only=True)

print(correlation)

print(correlation['GLD'])

plt.figure(figsize=(8,8))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f',annot=True, annot_kws={'size':8}, cmap='Blues')

sns.distplot(data['GLD'],color='black')

X=data.drop(['Date','GLD'],axis=1)
Y=data['GLD']

print(X)

print(Y)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)

model=RandomForestRegressor(n_estimators=100)

model.fit(X_train,Y_train)

test_data_prediction=model.predict(X_test)

print(test_data_prediction)

error=metrics.r2_score(Y_test,test_data_prediction)
print("The r^2 squaured error is given as ",error)

Y_test=list(Y_test)

plt.plot(Y_test,color='green',label='Actual Values')
plt.plot(test_data_prediction,color='red',label='Predicted Values')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()
plt.show()

