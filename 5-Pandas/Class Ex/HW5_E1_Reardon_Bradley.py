#E.1:

# i. ii. iii

import pandas as pd
import numpy as np
import io
import requests

data2 = 'https://learn-us-east-1-prod-fleet02-xythos.content.blackboardcdn.com/5fd21eff2f29a/6935826?X-Blackboard-Expiration=1614816000000&X-Blackboard-Signature=zlJJSl%2Bu%2FNWzvPhp8cOU%2FSQGArMow1%2FF1uVCQ0WTb0c%3D&X-Blackboard-Client-Id=105287&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Data2.txt&response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210303T180000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5SJBSTP6%2F20210303%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=2df732c8c487db7c5c61cdda9275e8361c13749c1a2d8dbc98c11dd14f3ffaaf'
s = requests.get(data2).content
chipotle = pd.read_csv(io.StringIO(s.decode('utf-8')), sep='\t')

# v.
chipotle['item_price'] = chipotle['item_price'].replace({'\$':''}, regex = True)
chipotle['item_price'] = chipotle['item_price'].astype(float)

# v.
chipotle_new = chipotle.drop_duplicates(subset=['item_name', 'quantity'])

# vi.
chipotle_new.loc[(chipotle_new['quantity'] == 1) & (chipotle_new['item_price'] > 10)]

# vii.
print(chipotle_new[['item_name', 'item_price']])

#viii.
print(chipotle_new.sort_values('item_name'))

# ix.
print(chipotle_new.iloc[chipotle_new['item_price'].argmax()])

#x.
print(chipotle[chipotle['item_name'] == 'Veggie Salad Bowl'].count())

#xi.
print(chipotle[(chipotle['item_name'] == 'Canned Soda') & (chipotle['quantity'] > 1)].count())