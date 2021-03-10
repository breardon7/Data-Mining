#E3

# i – iii.

import pandas as pd
import numpy as np
import io
import requests

users = pd.read_csv('data.txt', sep='|')
users.head(6)

# iv.
print(users.groupby('occupation').mean('age'))

# v.
user_male = users[users['gender'] == 'M']
user_female = users[users['gender'] == 'F']
male_ratio = user_male.groupby('occupation').count()['gender']/user_female.groupby('occupation').count()['gender']
print(pd.DataFrame(male_ratio).sort_values('gender', ascending = False))

# vi.
print(users.groupby('occupation').max('age'))
print(users.groupby('occupation').min('age'))

# vii.
print(users.groupby(['occupation', 'gender']).mean('age'))

#viii.

print(user_male.groupby('occupation').count()['gender']/(user_male.groupby('occupation').count()['gender'] + user_female.groupby('occupation').count()['gender']))
print(user_female.groupby('occupation').count()['gender']/(user_male.groupby('occupation').count()['gender'] + user_female.groupby('occupation').count()['gender']))