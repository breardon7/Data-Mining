# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 13 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Support Vector Machine  %%%%%%%%%%%%%%%%%
#%%-----------------------------------------------------------------------
# Exercise
#%%-----------------------------------------------------------------------
# Specify what are your features and targets. Why this is a classification
# 1- Use the voice dataset.
# 2- Specify what are your features and targets.
# 3- Why this is a classification problem.
# 4- Run the Support Vector Machine algorithm.
# 5- Explain your findings and write down a paragraph to explain all the results.
# 6- Explain the differences between Support Vector Machine and Logistic Regression.
#%%-----------------------------------------------------------------------
# 1-
import pandas as pd

df = pd.read_csv('voice.csv')

df_columns = df.columns
#%%-----------------------------------------------------------------------
# 2-

features = df.values[:,:20]
target = df.values[:,20]

#%%-----------------------------------------------------------------------
# 3-
'''
This is a classification problem because we are trying to classify 
observations as a male or female voice based on the given features' values.
'''

#%%-----------------------------------------------------------------------
# 4-
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import classification_report

le = LabelEncoder()

X = features
y_data = target

svm = SVC()

y = le.fit_transform(y_data)

X_train, X_test, y_train, y_test = train_test_split(X, y)

clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Classification Report: ")
print(classification_report(y_test,y_pred))
print("\n")


#%%-----------------------------------------------------------------------
# 5-

#%%-----------------------------------------------------------------------
# 6-