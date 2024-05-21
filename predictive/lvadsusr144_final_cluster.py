# -*- coding: utf-8 -*-
"""LVADSUSR144_final_cluster.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10YwUwidQYl3NJ9iL9YsJOfRpEhisIGAY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings("ignore")

#data loading
data = pd.read_csv("/content/Credit Card Customer Data.csv")
data.head()

#we dont need S1_No amd customer key
data.drop(columns=['Sl_No'],inplace=True)

data.drop(columns=['Customer Key'],inplace=True)

data.head()

data.shape

data.describe()

data.info()

#null values,duplicates,outliers - preprocessing

data.isnull().sum()

#we have 13 null values in total visits online so we need bivariate to see its skwedness and fill null
sns.histplot(data['Total_visits_online'])

#its is better to fill null values with median visits
data['Total_visits_online']=data['Total_visits_online'].fillna(data['Total_visits_online'].median())

data.isnull().sum()

data.duplicated().sum()
#there are no duplicates

#check for outliers

for c in data.select_dtypes(include=['int64','float64']).columns:
  plt.figure(figsize=(10,10))
  sns.boxplot(data[c])
  plt.title(f"Box plot of {c}")

# we have outliers in avg_credit_card_limit which must be treated

#handling outliers
q1 = data['Avg_Credit_Limit'].quantile(0.25)
q3= data['Avg_Credit_Limit'].quantile(0.75)
iqr = q3-q1
low = q1-1.5*iqr
up = q3+1.5*iqr
data.loc[data['Avg_Credit_Limit']<low,c]=low
data.loc[data['Avg_Credit_Limit']>up,c]=up

#check for correlation

plt.figure(figsize=(20,10))
sns.heatmap(data.corr(),annot=True)

#scatter plots

numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
for i in range(len(numerical_columns)):
    for j in range(i + 1, len(numerical_columns)):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=data, x=numerical_columns[i], y=numerical_columns[j])
        plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
        plt.show()

#feature selection
# based on my domain knowledge and bivariate analysis its better to choose avg_credit_limit and num of visit online to cluster the customers
df = data[['Avg_Credit_Limit','Total_visits_online']]

#finding the optimal cluster number
sse=[]
k_range = range(1,11)
for k in k_range:
  km = KMeans(n_clusters=k)
  km.fit(df)
  sse.append(km.inertia_)
plt.plot(k_range,sse,marker="o")
plt.xlabel('k')
plt.ylabel('sse')

#we can choose clusters = 3
#model implementation
km = KMeans(n_clusters=3)
y_pred = km.fit_predict(df)
df['clusters']=y_pred

df.head()

#plotting
df1 = df[df.clusters==0]
df2 = df[df.clusters==1]
df3 = df[df.clusters==2]
plt.scatter(df1['Avg_Credit_Limit'],df1['Total_visits_online'],color='green')
plt.scatter(df2['Avg_Credit_Limit'],df2['Total_visits_online'],color='blue')
plt.scatter(df3['Avg_Credit_Limit'],df3['Total_visits_online'],color='red')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],marker="*",color="black",label="Centroid")
plt.xlabel("Avg credit limit")
plt.ylabel("Total visits online")

#evaluation
print("silhoutte_score:",silhouette_score(df,y_pred))

#cluster profiling
df1.mean()
#the first cluster has customers who have low credit limit and they make less online transactions

df2.mean()

#the second cluster has customers who have credit limit greater than the lower but yet few have the habit of making more online visits
# this clusters has potential for improvement as they have the ability to spend more

df3.mean()

#the third cluster are high valued customers they have high credit limit and can see their high activity in online

#Business Recommendation

"""
The customers in first clusters can be given initial offers for making them to shift to make online visits
to take in more transactions

The customers in the second clusters should be focused on giving more discount on using credit so that the low visiters in this cluster gets
converted to high visiters

The customers in the third cluster need to be maintained through customer satisfaction , by giving premium offers like
airport transit options using credits etc
"""