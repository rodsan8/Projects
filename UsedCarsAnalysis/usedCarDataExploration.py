# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv('vehicles.csv')

df.shape

df.head()
df.tail()

df.columns

df.info()

df.describe()

# prints all null values
df.isnull()

# prints boolean if columns have null values
df.isnull().any()

# prints number of null values in each column
df.isnull().sum()

# prints percentage of null values on rows
df.isnull().sum() / df.shape[0]


df.type
# or (same thing)
df['type']

df.type.unique()

df.type.value_counts()

df.type.value_counts() / df.type.notnull().sum()

# Graphs #

df.year

df.year.plot(kind = 'hist')
df.year.hist()
df.year.hist(bins = 50)

df.type.value_counts()

df.type.value_counts().plot(kind = 'bar')
