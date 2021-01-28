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
from random import randrange

l = ['a','b','c','d']

def rand_perms(x):
    for i in range(len(x)):
        y = randrange(0, len(x))

        print(x[y], end=', ')

rand_perms(l)

from random import shuffle
l = ['a','b','c','d']
def shuffle_list(x):
    shuffle(x)
    print(x)
shuffle_list(l)



# =================================================================
# Class_Ex4:
# Write a program to convert a tuple to a string.
# ----------------------------------------------------------------
tuple = ('Hello','world!')

def tup_to_list(x):
    y = ', '.join(x)
    print(y)

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
tup2 = ('a','b','c','d')

def tup_exist(x, y):
    if y in x:
        print(str(y) + ' exists in: ' + str(x))
    else:
        print(str(y) + ' DOES NOT exist in: ' + str(x))

tup_exist(tup2, 1)
tup_exist(tup2, 'a')



# =================================================================
# Class_Ex7:
# Write a  program to check a list is empty or not.
# ----------------------------------------------------------------
list2 = [1,2,3,4]
list3 = []

def is_list_empty(x):
    if x == []:
        print('List is empty.')
    else:
        print('List is not empty.')

is_list_empty(list2)
is_list_empty(list3)


# =================================================================
# Class_Ex8:
# Write a program to generate a 4*5*3 3D array that each element is O.
# ----------------------------------------------------------------

def create_3d_array():
    y = [[0,0,0]]
    z = [y*5]
    a = z*4
    print(a)
create_3d_array()



