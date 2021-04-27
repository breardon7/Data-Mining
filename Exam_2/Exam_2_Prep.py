#%%-----------------------------------------------------------------------
# Import Necessary Packages
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
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans

from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score, roc_curve, roc_auc_score
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OneHotEncoder

#%%-----------------------------------------------------------------------
# Read in dataset
#%%-----------------------------------------------------------------------

df = pd.read_csv('')
print(df.shape)
print(df.columns)

#%%-----------------------------------------------------------------------
# Preprocessing
#%%-----------------------------------------------------------------------
# Rename columns

df.columns =

# Check NA value count
null_values = df.isnull().sum()
print(null_values[null_values > 0])

# Drop columns
df.drop()



# %%-----------------------------------------------------------------------
# Create train and test sets
# create separate df with modifications if necessary

df_mod = df[column_name] = 1

X = df.values[all features but target]
y = df.values[target feature]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# %%-----------------------------------------------------------------------
# Apply label encoder to features where necessary
le = LabelEncoder()
y = le.fit_transform(y)
df[column_name] = le.fit_transform(df[column_name])

#%%-----------------------------------------------------------------------
# Cross Validation
#%%-----------------------------------------------------------------------

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
# KNN CV
knn_classifier = KNeighborsClassifier()
print('KNN CV: ', cross_val_score(knn_classifier, X, y, cv=10, scoring = 'accuracy').mean())

# %%-----------------------------------------------------------------------
# Logistic Regression CV
logit_classifier = LogisticRegression()
print('KNN CV: ', cross_val_score(logit_classifier, X, y, cv=10, scoring = 'accuracy').mean())

#%%-----------------------------------------------------------------------
# Modeling
#%%-----------------------------------------------------------------------

# %%-----------------------------------------------------------------------
# %%-----------------------------------------------------------------------
# %%-----------------------------------------------------------------------
# Random Forest model
rf_clf = RandomForestClassifier(n_estimators=100)
rf_clf.fit(X_train, y_train)

# RF Feature Importance
importances = rf_clf.feature_importances_
f_importances = pd.Series(importances, data.iloc[:, 1:].columns)
f_importances.sort_values(ascending=False, inplace=True)

newX_train = X_train[:, rf_clffeature_importances_.argsort()[::-1][:15]]
newX_test = X_test[:, rf_clf.feature_importances_.argsort()[::-1][:15]]

rf_clf2 = RandomForestClassifier(n_estimators=100)
rf_clf2.fit(newX_train, y_train)

# Random Forest Predictions
rf_y_pred = rf_clf2.predict(newX_test)
rf_y_pred_score = rf_clf2.predict_proba(newX_test)

# Random Forest Results

print("\n")
print("Random Forest Results: \n")

print("Classification Report: ")
print(classification_report(y_test, rf_y_pred))
print("\n")

print("Accuracy : ", accuracy_score(y_test, rf_y_pred) * 100)
print("\n")

print("ROC_AUC : ", roc_auc_score(y_test,rf_y_pred_score[:,1]) * 100)

# %%-----------------------------------------------------------------------
# Random Forest Confusion Matrix
'''
conf_matrix = confusion_matrix(y_test, rf_y_pred)
class_names = nv_df_mod['q23_which_candidate_supporting'].unique()


df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names )

plt.figure(figsize=(5,5))

hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)

hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
plt.ylabel('True label',fontsize=20)
plt.xlabel('Predicted label',fontsize=20)
# Show heat map
plt.tight_layout()
plt.show()
'''
# %%-----------------------------------------------------------------------
# SVM model
# kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’}, default=’rbf’
svm_clf = SVC(kernel="linear")
svm_clf.fit(X_train, y_train)

# SVM Predictions
svm_y_pred = svm_clf.predict(X_test)
svm_y_pred_score = svm_clf.predict_proba(X_test)

# SVM Results

print("\n")
print("SVM Results: \n")

print("Classification Report: ")
print(classification_report(y_test, svm_y_pred))
print("\n")

print("Accuracy : ", accuracy_score(y_test, svm_y_pred) * 100)
print("\n")

print("ROC_AUC : ", roc_auc_score(y_test,svm_y_pred_score[:,1]) * 100)

def coef_values(coef, names):
    imp = coef
    print(imp)
    imp,names = zip(*sorted(zip(imp.ravel(),names)))

    imp_pos_10 = imp[-10:]
    names_pos_10 = names[-10:]
    imp_neg_10 = imp[:10]
    names_neg_10 = names[:10]

    imp_top_20 = imp_neg_10+imp_pos_10
    names_top_20 =  names_neg_10+names_pos_10

    plt.barh(range(len(names_top_20)), imp_top_20, align='center')
    plt.yticks(range(len(names_top_20)), names_top_20)
    plt.show()

# get the column names
features_names = X.columns

# call the function
coef_values(svm_clf.coef_, features_names)
#

# %%-----------------------------------------------------------------------
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

# %%-----------------------------------------------------------------------
# KNN model
stdsc = StandardScaler()
stdsc.fit(X_train)

X_train_std = stdsc.transform(X_train)
X_test_std = stdsc.transform(X_test)

knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train_std, y_train)


# KNN Predictions
knn_pred = knn_clf.predict(X_test_std)
knn_score = knn_clf.predict_proba(X_test)

# KNN Results
print("\n")
print("Results Using KNN & All Features: \n")

print("Classification Report: ")
print(classification_report(y_test,knn_pred))
print("\n")

print("Accuracy : ", accuracy_score(y_test, knn_pred) * 100)

# %%-----------------------------------------------------------------------
# Logistic Regression model
# convert multi-class label to binary (tweak parameters in lambda function)
df[target] = df[target].apply(lambda x:0 if x<=5 else 1)

logit_clf = LogisticRegression()
logit_clf.fit(X_train, y_train)


# Logistic Regression Predictions
logit_pred = knn_clf.predict(X_test_std)
logit_score = knn_clf.predict_proba(X_test)

# Logistic Regression Results
print("\n")
print("Results Using KNN & All Features: \n")

print("Classification Report: ")
print(classification_report(y_test,logit_pred))
print("\n")

print("Accuracy : ", accuracy_score(y_test, logit_pred) * 100)

# %%-----------------------------------------------------------------------
# Naive Bayes model
nb_clf = GaussianNB()
nb_clf.fit(X_train, y_train)


# Logistic Regression Predictions
nb_pred = knn_clf.predict(X_test_std)
nb_score = knn_clf.predict_proba(X_test)

# Logistic Regression Results
print("\n")
print("Results Using KNN & All Features: \n")

print("Classification Report: ")
print(classification_report(y_test,nb_pred))
print("\n")

print("Accuracy : ", accuracy_score(y_test, nb_pred) * 100)

# %%-----------------------------------------------------------------------
# K-means model

kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

#%%-----------------------------------------------------------------------
# Correlation Matrix
#%%-----------------------------------------------------------------------
'''
corrMatrix = df.corr()
sns.heatmap(corrMatrix)
plt.show()
'''

