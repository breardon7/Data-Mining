#E2

# i.ii.
import pandas as pd
import numpy as np
food = pd.read_csv('Food.tsv', sep='\t')

# iii.
print(food.size)
print(food.head(6))

# iv.
print(food.columns)
print(len(food.columns))

# v.
print(food.columns[104])
print(food['-glucose_100g'].dtype)

# vi.
print(food.index)
print(food.index.shape)

#vii.
print(food['product_name'].iloc[99])