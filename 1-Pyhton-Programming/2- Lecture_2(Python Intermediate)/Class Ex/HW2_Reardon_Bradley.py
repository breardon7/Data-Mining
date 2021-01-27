# =================================================================
# Class_Ex1:
# Write a program that simulates the rolling of a die.
# ----------------------------------------------------------------
from random import randrange
x = randrange(0,7)
print('+---------+')
print('|' + (' '*9) +'|')
print('|' + (' '*4) + str(x) + (' '*4) +'|')
print('|' + (' '*9) +'|')
print('+---------+')


# =================================================================
# Class_Ex2:
# Answer  Ex1 by using functions.
# ----------------------------------------------------------------
def dice_roll():
    x = randrange(0, 7)
    print('+---------+')
    print('|' + (' ' * 9) + '|')
    print('|' + (' ' * 4) + str(x) + (' ' * 4) + '|')
    print('|' + (' ' * 9) + '|')
    print('+---------+')

dice_roll()




# =================================================================
# Class_Ex3: 
# Randomly Permuting a List
# ----------------------------------------------------------------
list = ['a','b','c']
def rand_perm(x):
    r, s, t = randrange(0,len(x)), randrange(0,len(x)), randrange(0,len(x))
    print(x[r]+x[s]+x[t])

rand_perm(list)





# =================================================================
# Class_Ex4:
# Write a program to convert a tuple to a string.
# ----------------------------------------------------------------
tuple = ('Hello','goodbye')

def tup_to_list(x):
    for i in x:
        i = [i]
        print(x, type(x))

tup_to_list(tuple)



# =================================================================
# Class_Ex5:
# Write a program to get the 3th element of a tuple.
# ----------------------------------------------------------------
tup = (1,2,7,4)

def third_tup(x):
    y = x[2]
    print(y)
third_tup(tup)


# =================================================================
# Class_Ex6:
# Write a program to check if an element exists in a tuple or not.
# ----------------------------------------------------------------




# =================================================================
# Class_Ex7:
# Write a  program to check a list is empty or not.
# ----------------------------------------------------------------




# =================================================================
# Class_Ex8:
# Write a program to generate a 4*5*3 3D array that each element is O.
# ----------------------------------------------------------------





