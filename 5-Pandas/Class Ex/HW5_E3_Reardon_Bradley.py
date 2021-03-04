#E3

# i – iii.

import pandas as pd
import numpy as np
import io
import requests

data = 'https://learn-us-east-1-prod-fleet02-xythos.content.blackboardcdn.com/5fd21eff2f29a/6935825?X-Blackboard-Expiration=1614826800000&X-Blackboard-Signature=tBHozFLxezqtBkweX%2F5z6rZczQllwdYaiP2lx9ekmdo%3D&X-Blackboard-Client-Id=105287&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Data.txt&response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210303T210000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5SJBSTP6%2F20210303%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=150d0d9075ee3a56f87e588966ebd228f00e0e94b5824863eada57f61e1795ad'
s = requests.get(data).content
users = pd.read_csv(io.StringIO(s.decode('utf-8')), sep='|')
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