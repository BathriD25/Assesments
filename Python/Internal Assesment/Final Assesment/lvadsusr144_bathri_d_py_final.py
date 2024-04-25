# -*- coding: utf-8 -*-
"""LVADSUSR144_BATHRI_D_PY_FINAL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n6wR1wlYFB0O-HTUEfsobaO0bDqBt_Iz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1a
data = pd.read_csv("/content/Final Dataset - IPL.csv")
data.head()

#1b
rows = data.shape[0]
col = data.shape[1]
print("rows:",rows)
print("Columns:",col)
data.info()

numerical = data.select_dtypes('int','float')
categorical = data.select_dtypes('object')
a = data.isnull().sum()
a

#2 a,b
a = data.isnull().sum()
b = data.duplicated().sum()
print(a)
print("-----")
print(b)
#the data has no missing values and duplicate values hence we are good to go

#3 descriptive statistics
print("Mean")
print("----")
print(numerical.mean())
print("Median")
print("-------")
print(numerical.median())
print("Mode")
print("-----")
print(numerical.mode())
print("range")
print("------")
print(numerical.max()-numerical.min())
print("variance")
print("----")
print(numerical.var())
print("standard deviation")
print("--------------------")
print(numerical.std())

#4 data visualisation

# I)histogram of first innings score
plt.figure(figsize=(10,6))
plt.hist(data['first_ings_score'],bins=12)
plt.title("Histogram of 1st innings score")
plt.show()

# II)scatter plot
plt.figure(figsize=(10,6))
plt.scatter(data['first_ings_score'],data['second_ings_score'])
plt.xlabel("first innings score")
plt.ylabel("seconf innings score")
plt.title("Scatter plot of 1st vs 2nd innings scores")
plt.grid()
plt.show()

# III)pie chart
data.head()
a = data['match_winner'].value_counts()
plt.pie(a,autopct="%1.1f%%",labels=a.keys())
plt.show()

#bar chart
a = (data['won_by'].value_counts())
plt.pie(a,autopct="%1.1f%%",labels=a.keys())
plt.title("Match wins by runs/wickets")
plt.show()

#5 correl heatmap
data.head()
correl = numerical[['first_ings_score','first_ings_wkts','second_ings_wkts','second_ings_score']].corr()
sns.heatmap(correl,annot=True)

#6 outlier detection
data.head()
plt.boxplot(data['first_ings_score'])
plt.title("Box Plot of first innings Runs")
plt.ylabel(" runs")
q1 = data['first_ings_score'].quantile(0.25)
q2 = data['first_ings_score'].quantile(0.75)
iqr = q2-q1
low= q1-1.5*iqr
up = q2+1.5*iqr
outlier  = data[(data['first_ings_score']<low)|(data['first_ings_score']>up)]
out = np.array(outlier['first_ings_score'])
print(out)
"""
The outlier in first innings run will affect when it comes to large
data sets as in few matches team would have won with a 1st inning runs higher than
than the low or upper bound as it would affect the average win by runs
"""

#7a
data.head()
#team performance across venues



#8a
#player of the match analysis
a = data['player_of_the_match'].value_counts().sort_values(ascending=False).head(10)
#impact of top scorers
print("Top 10 performers")
b = a.keys()
plt.bar(b,a)
a

"""#9 INSIGHTS

>



1. Our analysis begins with the cleaning the data and removing the duplicates value if present, but in our case it was nil.

2. while looking at the descriptive statistics of the numerical data we find that the average first innings score is greater than the second inning score which takes us to the next step.

3. while plotting a histogram(likelihood of 1st inning score) of the first innings score we find that many scores lies in the range of 170-180 which is a good score batting first.

4. now we tend to compate first inning score with that of the second inning score with a scatter plot now we can see a big cluster of runs in the range of 150-180 which gives us idea about the whole average score is around the same ballpark

5. To see how the ditribution of team wins we see their win percent infering
Gujarat to be with the most wins.

6. To check weather the team has won by runs or by wickets we plot a pie chart,
figured that the its 50-50 chance.

7. We check for any outlier in the 1st inning runs to see a single outlier with 67runs which is way below our avg of 170

8. while looking at the top 10 performer we could see more count of players from Gujrat and Rajastan supporting with the fact of being successfull franchise.
"""