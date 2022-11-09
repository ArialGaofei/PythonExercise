# -*- coding: utf-8 -*-
"""Churn-Demo-EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aoUaoP6DuTWMcmTYWxaruP77aQ2qt1Pq

# Mount Drive
"""

ls

from google.colab import drive
drive.mount('/content/drive')

# Project Directory path 
project_dir = 'drive/MyDrive/DAB103-DEMO/ChurnDemo/'

import glob

# Using '*' pattern 
print('\nNamed with wildcard *:')
for name in glob.glob(project_dir+'*'):
    print(name)

print(project_dir+'*')

# Using '*' pattern
print('\nNamed with wildcard *:')
for name in glob.glob(project_dir+'*.csv'):
    print(name)

import pandas as pd
churn = pd.read_csv(project_dir+ 'Churn-Modelling.csv')

churn

type(churn)

#set the RowNumber (Column zero) as the DataFrame Index
#this replaces the default index created by pandas
#notice we have one less column (14 instead of 15)
churn = pd.read_csv(project_dir+ 'Churn-Modelling.csv', index_col=0)
churn

"""# Simple Exporatory Data Analysis (EDA)"""

churn.head(10)

churn.tail(10)

type(churn)

# rows and columns
churn.shape

type(churn.shape)

churn.shape[0]

churn.shape[1]

type (churn.shape[1])

churn.Gender == 'Male'

type(churn.Gender)

males =  churn[churn.Gender == 'Male']
males

type(males)

males.shape

males.shape[0]

males.shape[0]/churn.shape[0]

churn.info()

# all the content of column 13 is NaN (NaN), we can safely delete this column
churn['Unnamed: 14']

type(churn['Unnamed: 14'])

del churn['Unnamed: 14']

# we now have 13 columns
churn

churn.describe()

# overall correlations
churn.corr()

churn.describe(include=['O'])

g1 = churn.groupby(['Gender']).size(); g1

g1 = churn.groupby(['Geography']).size(); g1

"""# Additional EDA"""

Age = churn['Age']
Age

type(Age)

Age = churn.Age 
Age

type(Age)

Age.value_counts()

surnameCount = churn.groupby(['Surname'])['Age'].count().reset_index(
  name='Count').sort_values(['Count'], ascending=False)

surnameCount

Age.describe()

Age.mean()

g1 = churn.groupby(['Gender']).size(); g1

p1 = g1.plot(kind='bar', title='Gender Breakdown')

g1 = churn.groupby(['Geography']).size(); g1

p1 = g1.plot(kind='bar', title='Geography Breakdown')

help(pd)

"""# Solution by Ritesh Kush Kankonkar"""

churn2 = pd.read_excel(project_dir + 'Churn-Modelling.xlsx')

churn2

churn2.columns

df1 = churn2[churn2.columns]
df1["Exited"] = df1["Exited"].map({0: "Stayed", 1: "Exited"})
df1.head()

df1["Exited"]

# Note that we have two DataFrames.  We made a copy of churn into df1
churn2

df1["Exited"]

pivot1 = df1.pivot_table(index='Gender', columns='Exited', values='RowNumber', aggfunc="count")

pivot1

import matplotlib.pyplot as plt
import seaborn as sns

fig = pivot1.plot(kind="bar", stacked=True, color=["red","blue"])
plt.title("Churn rate by Gender")

pivot2 = df1.pivot_table(index='Geography', columns='Exited', values='RowNumber', aggfunc="count")
fig = pivot2.plot(kind="bar", stacked=True, color=["red","blue"])

plt.title("Churn rate by Country")

df1["age_bins"] = pd.qcut(df1["Age"], q=10)
pivot3 = df1.pivot_table(index="age_bins", columns="Exited", values="RowNumber", aggfunc="count")
fig = pivot3.plot(kind="bar", stacked=True, color=["red","blue"])

plt.title("Churn rate by Age Group")

df1["age_bins"]

df1

"""# Solution by Vishant Bhatia"""

churn3 = pd.read_excel(project_dir + 'Churn-Modelling.xlsx', index_col=0)

churn3

churn3["Surname"]

type (churn3["Surname"])

churn3[["Surname"]]

type (churn3[["Surname"]])

churn3[["Surname","Balance"]]

churn3.loc[[2]]

churn3.loc[[3]]

churn3.iloc[:,1]

churn3.loc[[2,4,5,8],["Surname","CreditScore","Balance"]]

churn3.loc[:,["Gender","Age"]]

churn3[['Gender','Age']]

churn3.iloc[[10,30,35,55]]

churn3.iloc[[55,78,12],[1,2,3,4,5]]

churn3.iloc[:,[1,2,3,4,5,6]]

churn3.loc[:,["Balance"]]

churn3.groupby(by = 'Gender')["Exited"].count().to_frame()

churn3.groupby(by = ['Gender','Exited']).count()

churn3.groupby(by = 'Gender')["Exited"].describe()

df_gender=churn3.loc[:,["Gender","Exited"]]
gender_groupby=df_gender.groupby("Gender",axis=0)
gender_groupby.count()