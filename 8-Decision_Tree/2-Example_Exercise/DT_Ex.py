# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 05 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Decision Tree  %%%%%%%%%%%%%%%%%%%%%%%%%%


#%%-----------------------------------------------------------------------
# Exercise
#%%-----------------------------------------------------------------------
# Specify what are your features and targets. Why this is a classification
# 1- Use the bank banknote dataset.
# 2- Specify what are your features and targets.
# 3- Why this is a classification problem.
# 4- Run the decision tree algorithm.
# 5- Explain your findings and write down a paragraph to explain all the results.
#%%-----------------------------------------------------------------------
# 1- Use the bank banknote dataset.
import pandas as pd
data = pd.read_csv('data_banknote_authentication.csv')
data.columns = ['Variance', 'Skewness', 'Curtosis', 'Entropy', 'Class']
#%%-----------------------------------------------------------------------
# 2- Specify what are your features and targets.

# The features are:
#   Variance of Wavelet Transformed image - Numeric (Variance)
#   Skewness of Wavelet Transformed image - Numeric (Skewness)
#   Curtosis of Wavelet Transformed image - Numeric (Curtosis)
#   Entropy of image - Numeric (Entropy)

# The targets are the classes which are: Genuine (Class = 0), Forged (Class = 1)


#%%-----------------------------------------------------------------------
# 3- Why this is a classification problem.

# This is a classification problem because we are trying to group the
# observations into classes based on the feature values for each observation.


#%%-----------------------------------------------------------------------
# 4- Run the decision tree algorithm.
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import webbrowser

X = data.values[:,0:4]
y = data.values[:,4]
class_le = LabelEncoder()
y = class_le.fit_transform(y)

X_test, X_train, y_test, y_train = train_test_split(X, y, test_size=0.2, random_state=50)

clf_gini = DecisionTreeClassifier(criterion="gini", random_state=50, max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)
clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=50, max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)
y_predict_gini = clf_gini.predict(X_test)
y_predict_entropy = clf_entropy.predict(X_test)
print('GINI Results: \n')
print(classification_report(y_test, y_predict_gini))
print('GINI Accuracy Score:', accuracy_score(y_test, y_predict_gini)*100)
print('\n')
print('Entropy Results: \n')
print(classification_report(y_test, y_predict_entropy))
print('Entropy Accuracy Score:', accuracy_score(y_test, y_predict_entropy)*100)
print('\n')
#%%-----------------------------------------------------------------------
# 5- Explain your findings and write down a paragraph to explain all the results.

# I found that the GINI accuracy score was 89.56 and the entropy accuracy
# score was 96.17, meaning the entropy method of classifying is a better method for
# this dataset. Both methods have high f1-scores which means the methods are correctly
# classifying most of the observations (low false positives and false negatives). The
# entropy f1-score being higher than the GINI f1-score shows that the entropy
# method correctly classifies observations more often than the GINI method.


