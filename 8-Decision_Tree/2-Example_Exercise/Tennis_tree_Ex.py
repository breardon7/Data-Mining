# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 05 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Decision Tree  %%%%%%%%%%%%%%%%%%%%%%%%%%
#%%-----------------------------------------------------------------------
#%%-----------------------------------------------------------------------
# Exercise
#%%-----------------------------------------------------------------------

# 1:
# Build the simple tennis table we just reviewed, in python as a dataframe. Label the columns.
# We are going to calculate entropy manually, but in python.
# Make sure to enter all variables as binary vs. the actual categorical names
# Name the dataframe tennis_ex.
#%%-----------------------------------------------------------------------
import pandas as pd
# data = {'outlook': ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'rainy'],
#        'temp': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
#        'humidity': ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal','high', 'normal', 'high'],
#        'windy': ['false', 'true', 'false', 'false', 'false', 'true', 'true', 'false', 'false', 'false', 'true', 'true','false', 'true'],
#        'play': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

#        }
data = {'outlook': [0, 0, 1, 2, 2, 2, 1, 0, 0, 2, 0, 1, 1, 2],
        'temp': [0, 0, 0, 1, 2, 2, 2, 1, 2, 1, 1, 1, 0, 1],
        'humidity': [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        'windy': [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1,0, 1],
        'play': [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]

        }
tennis_ex = pd.DataFrame(data = data)

#%%-----------------------------------------------------------------------
# 2:
# Build a function that will calculate entropy. Calculate entropy for the table we just went over
# in the example, but in python
# This is for the first split.
#%%-----------------------------------------------------------------------
import math

def entropy_func(feature):
    mylist = list(feature)
    distinct_list = list(set(mylist))
    e = 0
    total = len(mylist)
    count1 = 0
    count2 = 0
    if len(distinct_list) <= 2:
        for i in distinct_list:
            count = mylist.count(i)
            x = (-(count / total) * math.log2(count / total))
            e += x
        return e
    else:
        for i in distinct_list:
            if i == 1:
                count1 += mylist.count(i)
            else:
                count2 += mylist.count(i)
        return (-(count1 / total) * math.log2(count1 / total)) + (-(count2 / total) * math.log2(count2 / total))

outlook_ent = entropy_func(tennis_ex['outlook'])
temp_ent = entropy_func(tennis_ex['temp'])
humidity_ent = entropy_func(tennis_ex['humidity'])
windy_ent = entropy_func(tennis_ex['windy'])
play_ent = entropy_func(tennis_ex['play'])
print(outlook_ent)
print(temp_ent)
print(humidity_ent)
print(windy_ent)
print(play_ent)






#%%-----------------------------------------------------------------------
# 3:
# Run the decision tree algorithm and find out the best feature and graph it.
#%%-----------------------------------------------------------------------
# Importing the required packages
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import tree
import pydotplus
import collections
#%%-----------------------------------------------------------------------
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
#%%-----------------------------------------------------------------------

# Libraries to display decision tree
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import webbrowser
#%%--------------------------------Save Console----------------------------

# old_stdout = sys.stdout
# log_file = open("console.txt", "w")
# sys.stdout = log_file

#%%-----------------------------------------------------------------------
tennis = pd.read_csv('tennis.csv')
X = tennis_ex.values[:,:4]
y = tennis_ex.values[:,4]
clf = tree.DecisionTreeClassifier(random_state=11)
clf = clf.fit(X, y)

dot_data = tree.export_graphviz(clf,
                                feature_names=list(tennis.columns)[0:4],
                                out_file=None,
                                filled=True,
                                rounded=True
                                )
graph = pydotplus.graph_from_dot_data(dot_data)

colors = ('brown', 'forestgreen')
edges = collections.defaultdict(list)

for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))

for edge in edges:
    edges[edge].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[edge][i]))[0]
        dest.set_fillcolor(colors[i])

graph.write_png('tennis.png')
graph.write_svg('tennis.svg')


#X_test, X_train, y_test, y_train = train_test_split(X, y, test_size=0.2, random_state=100)



