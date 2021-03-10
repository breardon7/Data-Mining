#E.1:

# i. ii. iii

import pandas as pd
import numpy as np
import io
import requests

chipotle = pd.read_csv('data2.txt', sep = '\t')
#s = requests.get(data2).content
#chipotle = pd.read_csv(io.StringIO(s.decode('utf-8')), sep='\t')

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