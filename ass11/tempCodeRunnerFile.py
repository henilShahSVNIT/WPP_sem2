'''
Given a dataset of concerts, count the number of concerts per (artist, venue), per year
month. Make the resulting table be a wide table - one row per year month with a column
for each unique (artist, venue) pair. Use the cross product of the artists and venues Series
to determine which (artist, venue) pairs to include in the result.
'''
import pandas as pd

data={
    'date':['2025-05-17', '2025-04-21','2025-07-28','2025-07-29','2025-05-05'],
    'artist':['A','B','A','C','B'],
    'venue':['X','X','Y','Y','Z']
}

df=pd.DataFrame(data)
df['date']=pd.to_datetime(df['date'])
df['year_month']=df['date'].dt.to_period('M')
df['pair']=df['artist']+'_'+df['venue']

# print(df)

pivot=df.pivot_table(index='year_month', columns='pair', aggfunc='size', fill_value=0)
artists=df['artist'].unique()
venues=df['venue'].unique()
all_pairs=[f"{a}_{v}" for a in artists for v in venues]

for pair in all_pairs:
    if pair not in pivot.columns:
        pivot[pair]=0

# print(pivot)
pivot=pivot[all_pairs]

print(pivot)