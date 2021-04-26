import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

df = pd.read_csv('Tumor.csv')
print(df.head())
print(df.columns)

weight_mean = df[' Weight(grams)'].mean()
size_mean = df['Tumor Size(cm^3)'].mean()
size = np.array(df['Tumor Size(cm^3)'])
weight = np.array(df[' Weight(grams)'])


def linear_regression(x, y):
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()

    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean) ** 2).sum()
    B1 = B1_num / B1_den

    B0 = y_mean - (B1 * x_mean)

    return (B0, B1)

b0 = linear_regression(weight)
plt.plot(linear_regression(size, weight)[2])
plt.show()



m, b = np.polyfit(size, weight, 1)

plt.scatter(size, weight)
plt.plot(size, m*size +b)
plt.show()
