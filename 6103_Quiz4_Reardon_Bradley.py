# %% 1- Download the data_1 zip file from Blackboard. unzip the zip file by using zipfile package.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q1" + 20* "-")
import zipfile
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from zipfile import ZipFile

file_name = 'data_1.zip'
with ZipFile(file_name, 'r') as zip:
    zip.printdir()



# %% 2- Extract the the zip file using zipfile package and store the content into a data_1 folder (it has to be done automatically by os package).
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q2" + 20* "-")

with ZipFile(file_name, 'r') as zip:
    zip.extractall('data_1')





# %% 3- Read all the csv files and search for the csv file which has "Team" as column header.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q3" + 20* "-")

diamonds = pd.read_csv('diamonds.csv')
nba = pd.read_csv('nba.csv')

print('diamnods', diamonds.columns)
print('nba', nba.columns)

# NBA has a column header titled, 'Team'



# %% 4- Search for the followings.
# i. Find all the list of all unique teams and print out the total number.
# ii. Who gets the most salary and find out his age, position, and team .
# iii. Is there any trend between salary and age. Use linear regression and explain your results.

# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q4" + 20* "-")

print(nba["Team"].nunique())

nba_sal = nba.sort_values(by = 'Salary', ascending=False)

print(nba_sal.iloc[0][['Name', 'Team', 'Age', 'Position']])

nba2 = nba.dropna(subset=['Age', 'Salary'])
salary = np.array(nba2['Salary'])
age = np.array(nba2['Age'])

plt.scatter(age, salary)
plt.show()

correlation_matrix = np.corrcoef(age, salary)
correlation_xy = correlation_matrix[0,1]
print('correlation coefficient:', correlation_xy)

# Our correlation coefficient value of 0.21 shows that there is very little correlation between Age and Salary.


# %% 5- Read the other csv file and answer the following questions.
# i. Sort the entire DataFrame by the 'carat' Series in ascending and descending order.
# ii. Get randomly sample rows from diamonds DataFrame.
# iii. Get sample 75% of the DataFrame's rows without replacement and store the remaining 25% of the rows in another DataFrame.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q5" + 20* "-")


diamonds_carot_asc = diamonds.sort_values(by = 'carat')
diamonds_carot_desc = diamonds.sort_values(by = 'carat', ascending=False)

print(diamonds.sample(n = 10, axis=0))
diamond75 = diamonds.sample(frac=0.75, axis=0)
diamond25 = diamonds.loc[~diamonds.index.isin(diamond75.index), :]

print(diamond75)
print(diamond25)

