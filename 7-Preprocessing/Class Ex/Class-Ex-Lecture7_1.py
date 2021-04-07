# =================================================================
# Class_Ex1:  Convert text to lowercase
# ----------------------------------------------------------------
input_str = 'The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil.'

print(input_str.lower())

# =================================================================
# Class_Ex2:  Numbers removing

# ----------------------------------------------------------------
input_str = 'Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls.'

result = ''.join([i for i in input_str if not i.isdigit()])
print(result)

# =================================================================
# Class_Ex3: White spaces removal

# ----------------------------------------------------------------
input_str = "\t a string example\t "

print(input_str.replace(" ", ''))

# =================================================================
# Class_Ex4: Use Pandas and explore the given dataset.

# ----------------------------------------------------------------

import pandas as pd
import numpy as np

df = pd.io.parsers.read_csv('https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv',
     header=None, usecols=[0,1,2] )

df.columns=['Class label', 'Alcohol', 'Malic acid']
print(df.head())




# =================================================================
# Class_Ex5: Normalize the input of the IRIS dataset.

# ----------------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn import preprocessing

iris = load_iris()
print(iris.data.shape)
x = iris.data
y = iris.target
normalized_x = preprocessing.normalize(x)
print(normalized_x[:5])


# =================================================================
# Class_Ex6: Demonstrate data standardization of the Iris flowers dataset.
# ----------------------------------------------------------------

iris = load_iris()
x = iris.data
y = iris.target
standardized_x = preprocessing.scale(x)
print(standardized_x[:5])


# =================================================================
# Class_Ex7:

# ----------------------------------------------------------------
