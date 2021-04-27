#%%-----------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score, roc_curve, roc_auc_score
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer

#%%-----------------------------------------------------------------------
# Read in dataset
#%%-----------------------------------------------------------------------

df = pd.read_csv('Train.csv')
print(df.head())
print(df.shape)
'''print(df.columns)
print(df.dtypes)
print(df.info)'''

#%%-----------------------------------------------------------------------
# Preprocessing
#%%-----------------------------------------------------------------------
# Move Target to first column
target = 'Accident_Severity'
first_col = df.pop(target)
df.insert(0, target,  first_col)
df = df.replace({'Accident_Severity': {1:0, 2:0, 3:1}})

# Check NA value count
############ Check to see if null values are previously filled with zeroes or another value ############
null_values = df.isnull().sum().sort_values(ascending=False)
#print(null_values[null_values > 0])

# Drop Values with too many missing values
drop_cols = ['Junction_Detail']
df = df.drop(labels=drop_cols, axis = 1)
print(df.shape)

# Fill Missing Values (Simple Imputing)
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_median = SimpleImputer(missing_values=np.nan, strategy='median')
imp_mode = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
df = pd.DataFrame(imp_mode.fit_transform(df), columns=df.columns)
#print(df.isnull().sum())


# Transform categorical features
le = LabelEncoder()
df['Accident_Index'] = le.fit_transform(df['Accident_Index'])
df['Date'] = le.fit_transform(df['Date'])
df['Time'] = le.fit_transform(df['Time'])
df['Local_Authority_(Highway)'] = le.fit_transform(df['Local_Authority_(Highway)'])
df['Road_Type'] = le.fit_transform(df['Road_Type'])
df['Junction_Control'] = le.fit_transform(df['Junction_Control'])
df['Pedestrian_Crossing-Human_Control'] = le.fit_transform(df['Pedestrian_Crossing-Human_Control'])
df['Pedestrian_Crossing-Physical_Facilities'] = le.fit_transform(df['Pedestrian_Crossing-Physical_Facilities'])
df['Light_Conditions'] = le.fit_transform(df['Light_Conditions'])
df['Weather_Conditions'] = le.fit_transform(df['Weather_Conditions'])
df['Road_Surface_Conditions'] = le.fit_transform(df['Road_Surface_Conditions'])
df['Special_Conditions_at_Site'] = le.fit_transform(df['Special_Conditions_at_Site'])
df['Carriageway_Hazards'] = le.fit_transform(df['Carriageway_Hazards'])
df['Did_Police_Officer_Attend_Scene_of_Accident'] = le.fit_transform(df['Did_Police_Officer_Attend_Scene_of_Accident'])
df['LSOA_of_Accident_Location'] = le.fit_transform(df['LSOA_of_Accident_Location'])

# New Data
df_predict = pd.read_csv('Test_submission_netid_Ver_X.csv')

# Move Target to first column
target = 'Accident_Severity'
first_col = df_predict.pop(target)
df_predict.insert(0, target,  first_col)
df_predict = df_predict.drop(columns=['Junction_Detail'], axis = 1)



df_predict['Accident_Index'] = le.fit_transform(df_predict['Accident_Index'])
df_predict['Date'] = le.fit_transform(df_predict['Date'])
df_predict['Time'] = le.fit_transform(df_predict['Time'])
df_predict['Local_Authority_(Highway)'] = le.fit_transform(df_predict['Local_Authority_(Highway)'])
df_predict['Road_Type'] = le.fit_transform(df_predict['Road_Type'])
df_predict['Junction_Control'] = le.fit_transform(df_predict['Junction_Control'])
df_predict['Pedestrian_Crossing-Human_Control'] = le.fit_transform(df_predict['Pedestrian_Crossing-Human_Control'])
df_predict['Pedestrian_Crossing-Physical_Facilities'] = le.fit_transform(df_predict['Pedestrian_Crossing-Physical_Facilities'])
df_predict['Light_Conditions'] = le.fit_transform(df_predict['Light_Conditions'])
df_predict['Weather_Conditions'] = le.fit_transform(df_predict['Weather_Conditions'])
df_predict['Road_Surface_Conditions'] = le.fit_transform(df_predict['Road_Surface_Conditions'])
df_predict['Special_Conditions_at_Site'] = le.fit_transform(df_predict['Special_Conditions_at_Site'])
df_predict['Carriageway_Hazards'] = le.fit_transform(df_predict['Carriageway_Hazards'])
df_predict['Did_Police_Officer_Attend_Scene_of_Accident'] = le.fit_transform(df_predict['Did_Police_Officer_Attend_Scene_of_Accident'])
df_predict['LSOA_of_Accident_Location'] = le.fit_transform(df_predict['LSOA_of_Accident_Location'])

#df_predict = pd.DataFrame(imp_mode.fit_transform(df_predict), columns=df_predict.columns)


# Create train and test sets
# Test Data
X = df.values[:, 1:]
y = df.values[:, 0]
y=y.astype('int')
#print(np.unique(y))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# Feature Scaling
sc = StandardScaler()

X_scaled = sc.fit_transform(X)

sc.fit(X_train)
X_train_scaled = sc.transform(X_train)
X_test_scaled = sc.transform(X_test)

#%%-----------------------------------------------------------------------
# Cross Validation
#%%-----------------------------------------------------------------------
'''
# Random Forest CV
rf_classifier = RandomForestClassifier()
print('RF CV: ', cross_val_score(rf_classifier, X, y, cv=10, scoring = 'accuracy').mean())

# %%-----------------------------------------------------------------------
# SVM CV
svm_classifier = SVC()
print('SVM CV: ', cross_val_score(svm_classifier, X_scaled, y, cv=10, scoring = 'accuracy').mean())

# %%-----------------------------------------------------------------------
# Logistic Regression CV
logit_classifier = LogisticRegression()
print('Logit CV: ', cross_val_score(logit_classifier, X_scaled, y, cv=10, scoring = 'accuracy').mean())

# %%-----------------------------------------------------------------------
# KNN CV
knn_classifier = KNeighborsClassifier()
print('KNN CV: ', cross_val_score(knn_classifier, X_scaled, y, cv=10, scoring = 'accuracy').mean())

# %%-----------------------------------------------------------------------
# Naive Bayes CV
nb_classifier = GaussianNB()
print('Naive Bayes CV: ', cross_val_score(nb_classifier, X_scaled, y, cv=10, scoring = 'accuracy').mean())

# %%-----------------------------------------------------------------------
# Gradient Boosting CV
gb_classifier = GradientBoostingClassifier()
print('GB CV: ', cross_val_score(gb_classifier, X, y, cv=10, scoring = 'accuracy').mean())

'''
# Gradient Boosting model
gb_clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.05)
gb_clf.fit(X_train, y_train)

# Gradient Boosting Predictions
gb_pred = gb_clf.predict(X_test)
gb_score = gb_clf.predict_proba(X_test)

# Gradient Boosting Results

print("\n")
print("Results Using Gradient Boosting & All Features: \n")

print("Classification Report: ")
print(classification_report(y_test,gb_pred))
print("\n")

print("Accuracy : ", accuracy_score(y_test, gb_pred) * 100)
print("\n")

print("ROC_AUC : ", roc_auc_score(y_test,gb_score[:,1]) * 100)

#Train Data
X_new = df_predict.values[:, 1:]


new_output = gb_clf.predict(X_new)
print(new_output)

# df_predict['Accident_Severity'] = new_output
df_predict.to_csv(r'C:\Users\brear\OneDrive\Desktop\Grad School\DATS 6103\Data-Mining\Exam_2\Test_submission_Reardon_Bradley_Ver_X.csv', index=False)


'''
# Finalize model
import pickle
cart_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.05)
cart_model.fit(X_train, Y_train)

# Save model to disk
filename = '6103_Exam2_Final_Model.sav'
pickle.dump(cart_model, open(filename, 'wb'))

# Load model from disk and use it to make new predictions
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_validation, Y_validation)
print(result)

# Load test dataset
final_predict = pd.read_csv('Test_submission_netid_Ver_X.csv')
X_train = final_predict
pred = cart_model.predict(X_train)
print(pred)'''