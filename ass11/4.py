'''Whenever your friends John and Judy visit you together, y'all have a party. Given a
DataFrame with 10 rows representing the next 10 days of your schedule and whether John
and Judy are scheduled to make an appearance, insert a new column
called days_til_party that indicates how many days until the next party.
days_til_party should be 0 on days when a party occurs, 1 on days when a party doesn't
occur but will occur the next day, etc.'''

import pandas as pd

data = {
    'day': pd.date_range(start='2025-04-01', periods=10, freq='D'),
    'is_party_day': [False, False, True, False, False, False, False, True, False, False]
}

df = pd.DataFrame(data)

df['days_til_party'] = None

next_party_day = None

for i in range(len(df)-1, -1, -1):
    if df.loc[i, 'is_party_day']: 
        next_party_day = i 
    if next_party_day is not None:
        df.loc[i, 'days_til_party'] = next_party_day - i

print(df)