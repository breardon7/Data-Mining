# %%------------------------------------------------------------------------------
# Question 1:
# Hangman is a classic word game in which you must guess as many secret words as you can before time runs out! Challenge yourself.
# https://hangmanwordgame.com/?fca=1&success=0#/
# Write a computer program that simulate the following game.
# NOTE:  Write your own program.
# Your program should be as follows:
# your search word is DATAMINING.
# -- you will have 10 chances to predict the word. After that you should print a Game Over.
# -- The code should ask Enter the character you guess:
# -- Your guess is: ______ if it is not the character that you wanted.
# -- Your guess is: _A_A______ if you choose A.
# -- If you predict all the characters correctly then You win.

# %%--------------------------------Answer----------------------------------------------

print('Hangman Game')
#print('Guess a letter:', eval(input()))

#def hangman(x):











# %%-----------------------------------End-------------------------------------------
# Question 2:
"""
Create a Python class that mimics an API for a new website that publishes articles that users can comment on.
Each document in the API should be represented as a dictionary with structure:

{
article_title: "",
publish_date:"",
author:"",
comments:{
    username:"",
    comment_date:"",
    comment:""
    }
}

The documents should be stored in some type of python collection within a class object.
Your class should have methods that enable the following types of functionalities:

GET: Accepts one key-value pair argument. This should retrieve all documents with a given publish_date, author, or
article_title (only one at a time).
POST: Only accepts full document. This will add a new record to the API. Only the keys within the 'comment' section can
be empty when posting. All article titles are unique-- you can think of them as the unique identifier
PUT: Only accepts full document input. This will updates the values in the 'comment' key in the document, essentially
allowing people to comment on a post.
This method should be able to delete a 'comment' as well.
DELETE: Accepts a key value pair as input. This should delete an article with a given title, or all articles from a
given author from the server.

Your class should be able to handle common errors without breaking: commenting on a post that doesn't exist,
posting a post that is already on the server, none of the 'article_title', 'publish_date', or 'author' are empty
when adding a new document.
Note that you don't need to try and create every functionality that an
API would have. Only focus on the specific functionalities listed.
"""
# %%---------------------------------Answer---------------------------------------------


class API():
        #def __init__(self, GET, POST, PUT, DELETE):
                #self.get = GET
                #self.post = POST
                #self.put = PUT
                #self.delete = DELETE

        def get(self, x):
                return dict[x]









# %%-----------------------------------End-------------------------------------------
# Question 3:
# Graphs are networks that have nodes connected by edges or arcs.
# In directed graphs, the relationship between nodes have a direction,
# and are called arcs, in not directed graphs, the connections have no
# direction and are names edges. Assume we have the following graph.
# A -> B
# A -> C
# B -> C
# B -> D
# C -> D
# D -> C
# E -> F
# F -> C
# 1- Assign the following graph to a meaningful python variable and explain why that is the best.
# 2- Write a function to find a path between two nodes.
# It takes a graph (variable in 1) and the start and end as input. It will return a list of nodes
# 3- Change question number 2 code to find all the paths between a given start and end.
# 4- Change question number 3 and finds the closest or shortest path between two given start and end node.
# %%------------------------------------------------------------------------------

graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}
# A dictionary is the best way to represent the graph since the relationship between the nodes can essentially be
# thought of as a key: value pair since we have a directed graph.

def path_between(graph, x, y, z=[]):
        z = z + [x]
        if x not in graph.keys():
                return none
        if x == y:
                return [z]
        for i in graph[x]:
                if i not in z:
                        next = path_between(graph, i, y)
                        if next: return next
        return none

# %%-----------------------------------End-------------------------------------------
# Question 4:
"""
The stock for company A is valued at $100 and company B is valued a $50. 
After researching each company thoroughly, you discover that each company A's gain/loss each day will follow normal
distribution with mean of 1.7 and standard deviation of 0.5, and company B's gain/loss each day will follow a normal
distribution with mean of 3.2 and standard deviation 9.4. Use numpy random number generation to perform th following tasks
1. Estimate the probability that A will be greater than 150 after 30 days. 
2. Estimate the probability that B will be greater than 150 after 30 days.
3. Estimate the probability that A will be greater than B after 30 days.
4. Plot 1 possible simulation for the trends in A and B over the 30 days period on the same plot
"""

# %%------------------------------------------------------------------------------












# %%-----------------------------------End-------------------------------------------
# Question 5:
# Consider the following Python dictionary data and Python list labels, Answer the following questions
# 1- Create a DataFrame df from this dictionary data which has the index labels.
# 2- Display a summary of the basic information about this DataFrame and its data.
# 3- Return the first 3 rows of the DataFrame df.
# 4- Select just the 'animal' and 'age' columns from the DataFrame df
# 5- Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
# 6- Select only the rows where the number of visits is greater than 3.
# 7- Select the rows where the age is missing, i.e. is NaN.
# 8- Select the rows where the animal is a cat and the age is less than 3.
# 9- Select the rows the age is between 2 and 4 (inclusive).
# 10- Change the age in row 'f' to 1.5.
# 11- Calculate the sum of all visits (the total number of visits).
# 12- Calculate the mean age for each different animal in df.
# 13- Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame.
# 14- Count the number of each type of animal in df.
# 15- Sort df first by the values in the 'age' in decending order, then by the value in the 'visit' column in ascending order.
# 16- The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes'
# should be True and 'no' should be False.
# 17- In the 'animal' column, change the 'snake' entries to 'python'.
# 18- For each animal type and each number of visits, find the mean age. In other words, each row is an animal, each column
# is a number of visits and the values are the mean ages (hint: use a pivot table).

# %%------------------------------------------------------------------------------
import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd

data = pd.DataFrame(data)
print(data.describe())
print(data.head(3))
print(data[['animal', 'age']])
print(data.iloc[[3,4,8],[0,1]])
print(data[data['visits'] >3])
print(data[data['age'].isnull()])
print(data[(data['animal']=='cat') & (data['age'] < 3)])
print(data[(data['age'] > 1) & (data['age'] <5)])
# data = data.iloc['f','age'] = 1.5
print(sum(data['visits']))
print(data.groupby(by='animal').mean())
data['k'] = 0
data = data.drop('k', axis=1)
print(data.groupby(by='animal').count())
data = data.sort_values(['age', 'visits'], ascending = [False, True])
#data[data['priority'] == 'yes'] = True
#data[data['priority'] == 'no'] = False
#data[data['animal'] == 'snake'] = 'python'
#print(data.head(10))

pivot = data.pivot_table(index = 'animal',columns='visits',values='age', aggfunc='mean')



# %%-----------------------------------End-------------------------------------------
# Question 6:
# Amazon forest is 5.5 km square.It provides 20 % of oxygen of the world.
# The number of fires are recored in the amazon.csv file.
# Answer the following questions:
# %%------------------------------------------------------------------------------
# 1- Read the data into python.


amazon = pd.read_csv('amazon.csv', encoding='latin1')
print(amazon.head())


# 2- Print the state and the number of states.

print(amazon[['state','number']])





# 3- Find the total number of recoreds, mean of the number of
#  fires happened from 1998 to 2017 and highest number of fires ever
#  recorded.

print(amazon.shape[0])
print(amazon[(amazon['date'] > '1997-01-01') & (amazon['date'] < '2019-01-01')].mean())
print(amazon['number'].max())

# 4- Translate months (Portuguese) to english and replace them.





# 5- Visually show the sum of th efires over the year and dates. Did you find any trend?

import matplotlib.pyplot as plt

plt.bar(amazon['date'], amazon['number'])
plt.show()
plt.bar(amazon['year'], amazon['number'])
plt.show()
plt.bar(amazon['month'], amazon['number'])
plt.show()

# I dont see a trend. The number of fires seems to be consistent each year. March seems to have the least number of fires.

# 5- Find out at which year hightest total number of fire registered? and explore the reasons?


x = amazon.groupby(by=['year'])
print(x.max())

# The reason would be because of global warming.
