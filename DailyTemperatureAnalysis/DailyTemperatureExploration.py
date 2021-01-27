# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:29:52 2020

@author: adminSR
"""

#Import Functions
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#Read File
df = pd.read_csv("city_temperature.csv")

#View Rows and Columns
df.shape

#View First 5 Rows
df.head()

#View unique values in each column
df.nunique()

#Rename 'Region' column to 'Continent'
df.rename(index=str, columns={'Region':'Continent'}, inplace = True)

df.nunique() #check changes

#View Column names
df.columns

#View Column values
df.info()

#View Count, Mean, std, etc. of whole df
df.describe()

#view null values
df.isnull().sum()

# view Count for each continent
df['Continent'].value_counts()

#Graph Average Temperature Column
sns.distplot(df['AvgTemperature'])

#Create new df for hot/cold temperatures
hot_df = df[df.AvgTemperature >= 85]
cold_df = df[df.AvgTemperature <= 40]

#Graph Average Temperature Column of new df's
sns.distplot(hot_df['AvgTemperature'])
sns.distplot(cold_df['AvgTemperature'])

#decide whether hot, normal or cold & add to new column
df['Temperature_Status'] = df.AvgTemperature.apply(lambda x: 'Hot' if x >= 85 else ('Normal' if x < 85 and x > 40 else 'Cold'))             

df.head() #check changes

#Count of how many cold, normal or hot
df.Temperature_Status.value_counts()

df.Temperature_Status.describe()

#Make new df for only USA data

df.Country.unique()
df.Country.nunique()








