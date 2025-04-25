'''Write a Pandas program to convert all the string values to upper, lower cases in a given
pandas series. Also find the length of the string values.
s = pd.Series (['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])'''

import pandas as pd

s= pd.Series (['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper_case = s.str.upper()

lower_case = s.str.lower()

lengths = s.str.len()

df = pd.DataFrame({
    "Original":s,
    "Uppercase":upper_case,
    "Lowercase":lower_case,
    "Length":lengths
})

print(df)