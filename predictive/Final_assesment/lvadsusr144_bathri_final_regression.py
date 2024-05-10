# -*- coding: utf-8 -*-
"""LVADSUSR144_BATHRI_FINAL_REGRESSION.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lgjfRYeHYTNgdi0svLgIECkAnnQVNyJx
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

# load data
data = pd.read_csv("/content/Fare prediction.csv")
data.head()

data.info()

data['pickup_datetime']=pd.to_datetime(data['pickup_datetime']).dt.hour
data.head()

data.shape

data.isnull().sum()
#thus the data has no null values

data.duplicated().sum()
#the data has no duplicates

#outliers
plt.figure(figsize=(10,10))
sns.boxplot(data)

df = data[['fare_amount','pickup_datetime']]

# we only need fare amount and passenger count to predict so we keep the fares

x = df.drop(columns='pickup_datetime')
y = df['pickup_datetime']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
print("Mean Squared Error: ",mse)
rmse = mean_squared_error(y_test,y_pred,squared=False)
print("Root Mean Squared Error: ",rmse)
r2_s = r2_score(y_test,y_pred)
print("R2 Score",r2_s)