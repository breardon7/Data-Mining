#%%-----------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score, roc_curve, roc_auc_score
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

#%%-----------------------------------------------------------------------
# Read in dataset
#%%-----------------------------------------------------------------------

df = pd.read_csv('Kepler_Exoplanet.csv')
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)

#%%-----------------------------------------------------------------------
# Preprocessing
#%%-----------------------------------------------------------------------
# Move Target to first column
target = 'koi_disposition'
first_col = df.pop(target)
df.insert(0, target,  first_col)

# Transform categorical features
le = LabelEncoder()

df['kepoi_name'] = le.fit_transform(df['kepoi_name'])
df['kepler_name'] = le.fit_transform(df['kepler_name'])
df['kepler_name'] = le.fit_transform(df['kepler_name'])
df['koi_disposition'] = le.fit_transform(df['koi_disposition'])
df['koi_pdisposition'] = le.fit_transform(df['koi_pdisposition'])
df['koi_tce_delivname'] = le.fit_transform(df['koi_tce_delivname'])

# Check NA value count
############ Check to see if null values are previously filled with zeroes or another value ############
null_values = df.isnull().sum().sort_values(ascending=False)
print(null_values[null_values > 0])

# Drop Values with too many missing values
drop_cols = ['koi_teq_err1', 'koi_teq_err2', 'koi_score']
df = df.drop(labels=drop_cols, axis = 1)

# Fill Missing Values (Iterative Imputing)
imp = IterativeImputer(imputation_order='ascending', random_state=100, max_iter=100)
df = pd.DataFrame(imp.fit_transform(df), columns=df.columns)
null_values = df.isnull().sum().sort_values(ascending=False)
print(null_values[null_values > 0])


#null_values = df_new.isnull().sum().sort_values(ascending=False)
#print(null_values[null_values > 0])

# Create train and test sets

X = df.values[:, 1:]
y = df.values[:, 0]
#print(np.unique(y))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)


#%%-----------------------------------------------------------------------
# Cross Validation
#%%-----------------------------------------------------------------------
'''
# Random Forest CV
rf_classifier = RandomForestClassifier()
print('DF CV: ', cross_val_score(rf_classifier, X, y, cv=10, scoring = 'accuracy').mean())

# %%-----------------------------------------------------------------------
# SVM CV
svm_classifier = SVC()
print('SVM CV: ', cross_val_score(svm_classifier, X, y, cv=10, scoring = 'accuracy').mean())

# %%-----------------------------------------------------------------------
# Gradient Boosting CV
gb_classifier = GradientBoostingClassifier()
print('GB CV: ', cross_val_score(gb_classifier, X, y, cv=10, scoring = 'accuracy').mean())

# %%-----------------------------------------------------------------------
# Logistic Regression CV
logit_classifier = LogisticRegression()
print('Logit CV: ', cross_val_score(logit_classifier, X, y, cv=10, scoring = 'accuracy').mean())

# %%-----------------------------------------------------------------------
# KNN CV
knn_classifier = KNeighborsClassifier()
print('KNN CV: ', cross_val_score(knn_classifier, X, y, cv=10, scoring = 'accuracy').mean())

'''