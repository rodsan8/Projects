# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:17:03 2020

@author: adminSR
"""

import pandas as pd

df = pd.read_csv('vehicles.csv')

df.columns

df.describe()

# Remove Duplicates
df.drop_duplicates(inplace = True)

#Check for NULL values and % of NULL values
df.isnull()
df.isnull().any()
df.isnull().sum()
df.isnull().sum()/df.shape[0]

#remove null columns over a threshold (less than 60%)
lessthan60 = len(df)*.6
df.dropna(thresh=lessthan60, axis = 1).shape
df.dropna(thresh=21, axis = 0).shape

# Fill NaN's with a numeric value
df.odometer.fillna(df.odometer.median())
df.odometer.fillna(df.odometer.median()).isnull().any()

df.odometer.fillna(df.odometer.mean())
df.odometer.fillna(df.odometer.mean()).isnull().any()

# Normalize description (convert to all lowercase/uppercase)
df.description.head()
df.description.head().apply(lambda x: x.lower())
df.description.head().apply(lambda x: x.upper())

# float to string
df.description.astype(str).apply(lambda x: x.lower())
df.dtypes

# String to float
df.cylinders.head()
df.cylinders.dtype
df.cylinders.value_counts()

df.cylinders = df.cylinders.apply(lambda x: str(x).lower().replace('cylinders','').strip())
df.cylinders.value_counts()

df.cylinders = pd.to_numeric(df.cylinders, errors = 'coerce')
df.cylinders.value_counts()

df.cylinders.isnull().sum()

df.cylinders.fillna(df.cylinders.mean(), inplace =True)
df.cylinders.isnull().sum() #output should be 0

# visualizations (Histogram & Boxplots)
df.boxplot('odometer')
df.boxplot('price')

df.hist('odometer')
df.hist('price')

numeric = df._get_numeric_data()

# import modules
from scipy import stats
import numpy as np

#Removing outliers
outliers_price = df[(df.price < df.price.quantile(.995)) & (df.price > df.price.quantile(.005))]

outliers_price.boxplot('price')
outliers_price.hist('price')

outliers_odometer = df[(df.odometer < df.odometer.quantile(.995)) & (df.odometer > df.odometer.quantile(.005))]
outliers_odometer.boxplot('odometer')
outliers_odometer.hist('odometer')

#scaling data (for certain models)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaler.fit(df.cylinders.values.reshape(-1,1))
scaler.transform(df.cylinders.values.reshape(-1,1))

# OR

scaler.fit_transform(df.cylinders.values.reshape(-1,1))




