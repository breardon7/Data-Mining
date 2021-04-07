import pandas as pd
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
            if i < 2:
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