import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

#1 Examine the first few rows
print(ad_clicks.head())

#2 How many views came from each utm_source
ad_clicks.groupby('utm_source').user_id.count().reset_index()

#3 Create new column which is True if ad_click_timestamp is not null & False otherwise
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#4 Find % of people who clicked ads from each utm_source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

#5 pivot data
clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()

#6 new column, equal to % of users who clicked ad from each utm_source
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

#7 tells us whether the user was shown Ad A or Ad B.
print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())

#8 check to see if a greater percentage of users clicked on Ad A or Ad B.
print(ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index())

#9 create two DataFrames: a_clicks and b_clicks,contain only the results for A group and B group
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

#10 For each group, calculate % of users who clicked on the ad by day.
a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(columns='is_click', index='day', values='user_id').reset_index()

b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(columns='is_click', index='day', values='user_id').reset_index()

#11 Compare the results for A and B. 
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])

b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])

print(a_clicks_pivot)
print(b_clicks_pivot)
