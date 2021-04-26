# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 13 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% K-Nearest Neighbor  %%%%%%%%%%%%%%%%%%%%%
#%%-----------------------------------------------------------------------
# Exercise
#%%-----------------------------------------------------------------------
# Specify what are your features and targets. Why this is a classification
# 1- Use the chronic_kidney disease dataset.
# 2- Specify what are your features and targets.
# 3- Why this is a classification problem.
# 4- Run the K-Nearest Neighbor algorithm.
# 5- Explain your findings and write down a paragraph to explain all the results.
# 6- Explain the differences between Logistic Regression  and K-Nearest Neighbor.
#%%-----------------------------------------------------------------------
# 1-
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

col_names = ['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane', 'class']
df = pd.read_csv('chronic_kidney.csv', header=None, names=col_names)
print(df.shape)
print(df.head())
print(df.loc[:, 1])

#%%-----------------------------------------------------------------------
# 2-
X = df.values[:, :-1]
y = df.values[:, -1]


#%%-----------------------------------------------------------------------
# 3-
'''We are trying to classify each observation based their given feature values.'''

#%%-----------------------------------------------------------------------
# 4-
le = LabelEncoder()
df['rbc'] = le.fit_transform(df['rbc'])
df['pc'] = le.fit_transform(df['pc'])
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100, stratify=y)
stdsc = StandardScaler()
stdsc.fit(X_train)

X_train_std = stdsc.transform(X_train)
X_test_std = stdsc.transform(X_test)

clf = KNeighborsClassifier()
clf.fit(X_train_std, y_train)
y_pred = clf.predict(X_test_std)


print("\n")
print("Classification Report: ")
print(classification_report(y_test,y_pred))
print("\n")


print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
print("\n")

#%%-----------------------------------------------------------------------
# 5-

#%%-----------------------------------------------------------------------
# 6-