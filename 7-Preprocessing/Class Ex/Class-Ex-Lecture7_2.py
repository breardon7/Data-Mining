# =================================================================
# Class_Ex1:
# Lets using diabetes dataset as example. Load it using datasets package
# Print the size of the input and target dataset
# Print the features name
# ----------------------------------------------------------------

from sklearn.datasets import load_diabetes

diabetes = load_diabetes()

print('input', diabetes.data.size)
print('target', diabetes.target.size)
print('features', diabetes.feature_names)
print(diabetes.DESCR)

# =================================================================
# Class_Ex2:
# Using scikit-learn and create a test and train dataset
# ----------------------------------------------------------------

from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
x, y = np.arange(100).reshape(10,10), range(10)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.45)

#print(x_test)
#print(y_test)
# =================================================================
# Class_Ex3:
# Fit the model and test it on train/test values
# ----------------------------------------------------------------
from sklearn.linear_model import LinearRegression as lr

reg = lr().fit(x,y)

print('test score:', reg.score(x_test, y_test))
print('train score:', reg.score(x_train, y_train))



# =================================================================
# Class_Ex4:
# Print model coefficients
# ----------------------------------------------------------------

print('reg coef:', reg.coef_)




# =================================================================
# Class_Ex5:
# Predict the model using test input
# ----------------------------------------------------------------

print('reg predict:', reg.predict(x_test))


# =================================================================
# Class_Ex6:
# Plot a regression results
# ----------------------------------------------------------------

import matplotlib.pyplot as plt

plt.scatter(x_test[:,0], y_test, color='black')
plt.plot(x_test[:,1], reg.predict(x_test), color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()