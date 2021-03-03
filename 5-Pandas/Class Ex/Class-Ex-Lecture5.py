# =================================================================
# Class_Ex1:
# From the data table above, create an index to return all rows for
# which the phylum name ends in "bacteria" and the value is greater than 1000.
# ----------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({'value':[632, 1638, 569, 115, 433, 1130, 754, 555],
                     'patient':[1, 1, 1, 1, 2, 2, 2, 2],
                     'phylum':['Firmicutes', 'Proteobacteria', 'Actinobacteria',
    'Bacteroidetes', 'Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes']})

print(data[data.phylum.str.endswith('bacteria')&(data.value>1000)])

print('#',50*"-")
# =================================================================
# Class_Ex2:
# Create a treatment column and add it to DataFrame that has 6 entries
# which the first 4 are zero and the 5 and 6 element are 1 the rest are NAN
# ----------------------------------------------------------------

treatment = pd.Series([0,0,0,0,1,1])
data['treatment'] = treatment

print('#',50*"-")
# =================================================================
# Class_Ex3:
# Create a month column and add it to DataFrame. Just for month Jan.
# ----------------------------------------------------------------
data['month'] = 'Jan'


print('#',50*"-")
# =================================================================
# Class_Ex4:
# Drop the month column.
# ----------------------------------------------------------------
data = data.drop(columns='month')

print('#',50*"-")
# =================================================================
# Class_Ex5:
# Create a numpy array that has all the values of DataFrame.
# ----------------------------------------------------------------
np.array(data)
print('#',50*"-")

# =================================================================
# Class_Ex6:
# Read baseball data into a DataFrame and check the first and last
# 10 rows
# ----------------------------------------------------------------
baseball = pd.read_csv('baseball.csv')
baseball = pd.DataFrame(baseball)
print(baseball)
print('#',50*"-")
# =================================================================
# Class_Ex7:
# Create  a unique index by specifying the id column as the index
# Check the new df and verify it is unique
# ----------------------------------------------------------------
baseball_reindexed = baseball.set_index(baseball['id'])
baseball_reindexed.index.is_unique
print(baseball_reindexed)
print('#',50*"-")

# =================================================================
# Class_Ex8:
# Notice that the id index is not sequential. Say we wanted to populate
# the table with every id value.
# Hint: We could specify and index that is a sequence from the first
# to the last id numbers in the database, and Pandas would fill in the
#  missing data with NaN values:
# ----------------------------------------------------------------

id_range = np.arange(baseball['id'].min(), baseball['id'].max())

bball_all_id = baseball
bball_all_id['id'] = id_range
print('#',50*"-")

# =================================================================
# Class_Ex9:
# Fill the missing values
# ----------------------------------------------------------------


print('#',50*"-")

# =================================================================
# Class_Ex10:
# Find the shape of the new df
# ----------------------------------------------------------------


print('#',50*"-")

# =================================================================
# Class_Ex11:
# Drop row 89525 and 89526
# ----------------------------------------------------------------

print('#',50*"-")


# =================================================================
# Class_Ex12:
# Sor the df ascending and not ascending
# ----------------------------------------------------------------

print('#',50*"-")

