# -*- coding: utf-8 -*-
"""LVADSUSR144_BATHRI_D_IA2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14_A6fPL3aA_jruqhY22VlBPzcN53u2OK
"""

import numpy as np
import pandas as pd

#1

arr = np.array([1,2,3,4,5])
print("max:",arr.max())
print("min: ",arr.min())
print("mean: ",arr.mean())
print("standard deviation: ",arr.std())

#2
def normal(health):

health_data = np.array([[160, 70, 30],
                        [165, 65, 35],
                        [170, 75, 40]])
normal(health_data)

#3
marks = np.array([])

#4
arr = np.linspace(15,25,24)
print(arr)

#5
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5
a

#6
arr = np.arange()

#7
properties_matrix = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
print(properties_matrix.deter())

#8
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
condn = arr>5
print(arr[condn])

#9
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}
df = pd.DataFrame(data)
def age(ag):
  if ag>45:
    return True
  else:
    return False
def dept(dep):
  if dep!="HR":
    return True
  else:
    return False
df.apply(age(df["Age"]))
df.apply(dept(df["Department"]))
print(df)

#10
data = {'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Sales': [70000, 50000, 30000, 40000, 60000]}
df = pd.DataFrame(data)
res1 = df.groupby(['Salesperson','Department'])['Sales'].mean()
res1

#11
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}

#12
employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}
df1 = pd.DataFrame(employee_data)
df2 = pd.DataFrame(project_data)
df3 = pd.merge(df1,df2,on="Employee",how='left')
df3

#13
df = pd.read_csv("/content/Q13_sports_team_stats.csv")
df["win ratio"]=df["Wins"]/df["GamesPlayed"]
df["avg score"] = df.groupby("TeamID")["Wins"].mean()
df

df

#14
df = pd.read_csv("/content/Q14_customer_purchases.csv")
df["Date"]=pd.to_datetime(df["Date"]).dt.date
df['LoyaltyProgramSignUp']=pd.to_datetime(df['LoyaltyProgramSignUp']).dt.date
df1 = df.groupby('Date')['PurchaseAmount'].sum()
df2 = df.groupby("LoyaltyProgramSignUp")['PurchaseAmount'].sum()
print(df1)
print("++++++")
print(df2)

#15

df = pd.read_csv("/content/Q15_student_grades.csv")
df.groupby('Subject')["Grade"].mean().sort_values(ascending=True).head()
df