# =================================================================
# Class_Ex1:
# Write a NumPy code to test if none of the elements of a given
# array is zero.
# ----------------------------------------------------------------
import numpy as np

array_0 = np.arange(0, 10, 2)
array_no_0 = np.arange(1, 10, 2)


def contains_zero(x):
    if np.any(x == 0):
        print('Array contains zero values.')
    else:
        print('Array contains no zero values.')


contains_zero(array_0)
contains_zero(array_no_0)




# =================================================================
# Class_Ex2:
# Write a NumPy code to test if none of the elements of a given
# array is non-zero.
# ----------------------------------------------------------------

zero_array = np.zeros((3, 3))
one_array = np.ones((3, 4))


def contains_no_zero(x):
    if np.any(x != 0):
        print('Array contains non-zero values.')
    else:
        print('Array does not contain non-zero values.')


contains_no_zero(array_0)
contains_no_zero(array_no_0)
contains_no_zero(zero_array)
contains_no_zero(one_array)



# =================================================================
# Class_Ex3:
# Write a NumPy code to test if two arrays are element-wise equal
# within a tolerance.
# ----------------------------------------------------------------
x = np.zeros((3,4))
y = np.ones((3,4))
z = np.ones((3,4))

print(np.allclose(x,y))
print(np.allclose(y,z))



# =================================================================
# Class_Ex4:
# Write a NumPy code to create an array with the values
# 1, 8, 130, 10990005 and determine the size of the memory occupied
# by the array.
# ----------------------------------------------------------------

size = np.array([1, 8, 130, 10990005])

print('Array size: ', size.nbytes)





# =================================================================
# Class_Ex5:
# Write a NumPy code to create a array with values ​​ranging from
# 10 to 20 and print all values ​​except the first and last.
# ----------------------------------------------------------------

ten_twenty = np.random.randint(10,21, size=5)
print(ten_twenty)
print(ten_twenty[1:-1])



# =================================================================
# Class_Ex6:
# Write a NumPy code to reverse (flip) an array (first element becomes last).
# ----------------------------------------------------------------

import numpy as np

array_rev = np.array([1, 2, 3, 4])

def rev_array(x):
    y = []
    for i in reversed(x - 1):
        y += [x[i]]
    return np.array(y)


print(rev_array(array_rev))




# =================================================================
# Class_Ex7:
# Write a NumPy code to create a matrix with 1 on the border and 0 inside.
# ----------------------------------------------------------------

one_border = np.zeros((4,4))
one_border[0,:] = 1
one_border[-1,:] = 1
one_border[:,0] = 1
one_border[:,-1] = 1
print(one_border)



# =================================================================
# Class_Ex8:
# Write a NumPy code to add a border (filled with 0's) around a 3x3
# matrix of one.
# ----------------------------------------------------------------

zero_border = np.ones((4,4))
zero_border[0,:] = 0
zero_border[-1,:] = 0
zero_border[:,0] = 0
zero_border[:,-1] = 0
print(zero_border)





# =================================================================
# Class_Ex9:
# Write a NumPy code to append values to the end of an array.
# ----------------------------------------------------------------

x = np.zeros((3,4,5))
y = [1,2,3,4]
z = np.append(x,y)
print(z)





# =================================================================
# Class_E10:
# Write a NumPy code to find the set difference of two arrays.
# The set difference will return the sorted, unique values in array1
# that are not in array2.
# ----------------------------------------------------------------
array1 = np.arange(1,30,2)
array2 = np.arange(1,30,3)

print(np.setdiff1d(array1, array2))





# =================================================================
# Class_Ex11:
# Write a NumPy code to construct an array by repeating.
# Sample array: [1, 2, 3, 4, 5]
# ----------------------------------------------------------------

def repeat_array(x):
    y = []
    for i in range(x):
        y+= [i]
    return np.array(y)
print(repeat_array(10))




# =================================================================
# Class_Ex12:
# Write a NumPy code to get the values and indices of the elements
# that are bigger than 6 in a given array.
# ----------------------------------------------------------------

array6 = np.arange(0,30,5)

def above_six(x):
    y = []
    for i in range(len(x)):
        if x[i] > 6:
            y += [{i: x[i]}]
    return y

print(above_six(array6))



# =================================================================
# Class_Ex13:
# Write a NumPy program to find the 4th element of a 2 dimensional
# specified array.
# ----------------------------------------------------------------

D = np.array([1,2,3,4])
twoD = D.reshape((2,2))
Dflat = twoD.reshape((-1))
#I understand that I just reversed the initial reshape, but I
# wrote this solution as if the two-dimensional array was provided.
print(Dflat[3])


# =================================================================
# Class_Ex14:
# Write a NumPy code to get the floor, ceiling and truncated
# values of the elements of an numpy array.
# ----------------------------------------------------------------

fct = 4 * np.random.randn(1,5) + 4
floor = np.floor(fct)
ceiling = np.ceil(fct)
trunc = np.trunc(fct)
print(floor, ceiling, trunc)

# =================================================================
# Class_Ex15:
# Write a NumPy code to compute the factor of a given array by
# Singular Value Decomposition.
# ----------------------------------------------------------------

square = np.random.randint(1, 10, size = 4)
sq2 = square.reshape(2,2)
print(np.linalg.svd(sq2))




# =================================================================
# Class_Ex16:
# ----------------------------------------------------------------
# Write a NumPy code to compute the eigenvalues and right eigenvectors
# of a given square array.
# ----------------------------------------------------------------

print(np.linalg.eig(sq2))


# =================================================================
# Class_Ex17:
# Write a NumPy code to get the dates of yesterday, today and tomorrow.
# ----------------------------------------------------------------

print('Yesterday: ' + str(np.datetime64('today') + np.timedelta64(-1, 'D')))
print('Today: ' + str(np.datetime64('today')))
print('Tomorrow: ' + str(np.datetime64('today') + np.timedelta64(1, 'D')))



# =================================================================
# Class_Ex18:
# Write a NumPy code to find the first Monday in June 2021.
# ----------------------------------------------------------------




# =================================================================
# Class_Ex19:
# Write a NumPy code to find the roots of the following polynomials.
# a) x2 − 3x + 8.
# b) x4 − x3 + -x2 + 1x – 2
# ----------------------------------------------------------------





# =================================================================
# Class_Ex20:
# Write a NumPy program to calculate mean across dimension, of matrix.
# ----------------------------------------------------------------












