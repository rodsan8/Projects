# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 22:56:29 2020

@author: adminSR
"""

import pandas as pd

df = pd.read_csv('vehicles.csv')

# View Columns
df.columns

# Rename Columns
df2 = df.head(100)
df2.rename(index=str, columns={'region':'city'}, inplace = True)

# View Single Column
df2['city']

# View Rows
df2 [0:20]

# Selecting multiple columns 
url_city_price = df2[['url', 'city', 'price']]

# Selecting multiple columns (filter rows)
url_city_price3 = df2.iloc[0:99, 0:3]

# drop single column
data_drop = df2.drop('url', axis = 1)

# drop multiple columns
data_drop2 = df2.drop(['url','region_url'], axis = 1)

# Creating Column
df2['age'] = 2019 - df2['year']

df2['age']

# new cars age <= 10 (filtering)
data_new_cars = df2[df2.age <= 10]

data_new_cars2 = df2[(df2.age <= 10) | (df2.price > 5000)]

#new feauture creation
df2['price_per_mile'] = df2['price'] / df2['odometer']

# apply_function 
def price2x(x):
    return x*2

df2['price2'] = df2['price'].apply(price2x)

df2.price.head()
df2.price2.head()

# Labmda Function
df2['price3'] = df2.price.apply(lambda x: x*3)

df2.price3.head()

# Decide which cars are expensive and cheap
df2['isexpensive'] = df2.price.apply(lambda x: 'expensive' if x >10000 else 'cheap')

# how many cheap/expensive
df2.isexpensive.head(100).value_counts()

# new column based on info on two other columns
df2['new_cheap'] = df2.apply(lambda x: 'yes' if x['price'] < 10000 and x['age'] < 10 else 'no', axis = 1)

df2['new_cheap'].head(20)

df2['new_cheap'].head(20).value_counts()

#quantiles and bins
df2['price_quantile'] = pd.qcut(df2.price, 5)

df2['price_quantile'].value_counts()

pd.cut(df2.price, 5).value_counts()

# dummy variables
dummie_vars = pd.get_dummies(df2[['price','year','fuel','transmission', 'type']])

dummie_vars.head(50)

# Pivot table
pd.pivot_table(df2, index = 'year', columns = 'type', values = 'price', aggfunc = 'mean')
pd.pivot_table(df2, index = 'year', columns = 'type', values = 'price', aggfunc = 'mean').sort_index(ascending = False)
pd.pivot_table(df2, index = 'year', columns = 'type', values = 'price', aggfunc = 'mean').plot()


# Gropby
grouped_data = df2.groupby(['type','year'], as_index = False).mean()

# Merging dataframes
df3 = df2[['url','city']]
df4 = df2[['url','price']]

df_joined = pd.merge(df3, df4, on = 'url')

# Appending Dataframes
sampl1 = df.sample(100, random_state = 1)
sampl2 = df.sample(100, random_state = 2)

sampl1.append(sampl2)

#write to csv
df2.head(50).to_csv('top50.csv')


