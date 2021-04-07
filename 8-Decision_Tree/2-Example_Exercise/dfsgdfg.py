import pandas as pd
data = {'outlook': [0, 0, 1, 2, 2, 2, 1, 0, 0, 2, 0, 1, 1, 2],
        'temp': [0, 0, 0, 1, 2, 2, 2, 1, 2, 1, 1, 1, 0, 1],
        'humidity': [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        'windy': [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1,0, 1],
        'play': [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]

        }
tennis_ex = pd.DataFrame(data = data)

def entropy_func(feature):
    from scipy.stats import entropy
    mylist = list(feature)
    distinct_list = list(set(mylist))
    e = 0
    x = []
    total = len(mylist)
    for i in distinct_list:
        count = mylist.count(i)
        x.append(count/total)
    return entropy(x, base=2)


print(entropy_func(tennis_ex['outlook']))
print(entropy_func(tennis_ex['temp']))
print(entropy_func(tennis_ex['humidity']))
print(entropy_func(tennis_ex['windy']))
print(entropy_func(tennis_ex['play']))