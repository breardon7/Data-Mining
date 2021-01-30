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

# =================================================================
# E.1:
# Here is a search algorithm for arrays. The inputs are the array, which we call array; the number
# n of elements in array; and target, the number being searched for. The output is the index in
# array of target:
# 1. Let min = 0 and max = n-1.
# 2. Compute guess as the average of max and min, rounded down (so that it is an integer).
# 3. If array[guess] equals target, then stop. You found it! Return guess.
# 4. If the guess was too low, that is, array[guess] ¡ target, then set min = guess + 1.
# 5. Otherwise, the guess was too high. Set max = guess - 1.
# 6. Go back to step 2.
# i. Convert the following algorithm to a proper code and explain the process of the search. ii.
# What are the pro and cons of this method?
# ----------------------------------------------------------------


# =================================================================
# E.2:
# Work on a script to count the number of characters or (frequency) in a string.
# ----------------------------------------------------------------
string = "'Hello, my name is Brad.'"
def freq_of_string(x):
    count = 0
    for i in x:
        count += 1
    print('The frequency of ' + x + ' is: ' + str(count))

freq_of_string(string)

# =================================================================
# E.3:
# Write a function that takes a list of words and returns the length of the longest one.
# ----------------------------------------------------------------
long_list = ['hello', 'goodbye', 'brad', 'cat']


def longest_word(x):
    lengths = []
    for i in x:
        count = 0
        for j in i:
            count +=1
        lengths += [count]
        max = lengths[0]
        for k in lengths:
            if k > max:
                max = k
    print(max)

longest_word(long_list)

# =================================================================
# E.4:
# Make up your own list and work on a program to get the smallest number from the list
# ----------------------------------------------------------------
long_list = ['hello', 'goodbye', 'brad', 'cat']
def shortest_word(x):
    lengths = []
    for i in x:
        count = 0
        for j in i:
            count +=1
        lengths += [count]
        min = lengths[0]
        for k in lengths:
            if k < min:
                min = k
    print(min)

shortest_word(long_list)

# =================================================================
# E.5:
# Work on a function that takes two lists and returns same (or True) if they have at least one
# common element.
# ----------------------------------------------------------------
even = [2,4,6,8,]
odd = [1,3,5,7,]
mix = [1,2,3,4]

def common_element(x,y):
    for i in x:
        for j in y:
            if j == i:
                print('True')
                return
common_element(even,odd)
common_element(even,mix)

# =================================================================
# E.6:
# Work on a script to merge or join two dictionaries.
# ----------------------------------------------------------------


# =================================================================
# E.7:
# Work on a script or a program to map two lists into a dictionary.
# ----------------------------------------------------------------