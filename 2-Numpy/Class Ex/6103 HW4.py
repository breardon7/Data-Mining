# =================================================================
# E.1:
# Write a script to
# i. Sum all the items in a array (use random number generator and multiply it by 100, create a
# vector with the size 200).
# ii. Get the largest number and smallest number with the indexing of it.
# iii. plot the following vector and check your min and max value that you find in section i.
# ----------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

hundred = np.random.randint(0,100,200) * 100
sorted_hund = np.sort(hundred)
sum_hund= sum(hundred)
largest = sorted_hund[-1]
smallest = sorted_hund[0]

print(sum_hund)

plt.plot()

# =================================================================
# E.2:
# Plot the following functions x, sin(x), e**x
# and log(x) over the interval 1 < x < 6 with the step
# size of 0.1. (Put the title x axis label and y axis label for each plot)
# ----------------------------------------------------------------

x = np.arange(1,6,0.1)
y21 = x
y22 = np.sin(x)
y23 = np.exp(x)
y24 = np.log(x)
plt.plot(x, y21, c = 'b')
plt.plot(x, y22, c = 'y')
plt.plot(x, y23, c = 'r')
plt.plot(x, y24, c = 'g')
plt.title('Functions of X')
plt.xlabel('X')
plt.ylabel('Functions')
plt.ylim(-10,30)
plt.show()


# =================================================================
# E.3:
# Generate the random gaussian numbers with zero mean and variance of 1 called it vector x,
# generate the random uniform numbers with zero mean and variance of 1 called it vector y .
# i. Compute the mean and standard deviation of x and y.
# ii. Plot the histogram of x and y, increase the number of bins to get more resulting. Explain what
# information you get from the histogram(Put the title x axis label and y axis label for each plot)
# ----------------------------------------------------------------





# =================================================================
# E.4:
# A = ([1,2,3,4,5,6,7,8,9]) <--2-Dimensional 3x3
# Answer the following questions (Do not put the digits manually ):
# i. Assign vector x to the first row of A.
# ii. Assign matrix y to the last 2 rows of A
# iii. Sum the first row and add it to the first column.
# iv. Compute the norm of x (Euclidian Norm).
# v. Swap the first column with the second column and delate the second row.
# ----------------------------------------------------------------





# =================================================================
# E.5:
# i. Create a vector between 20 and 35, square each elements and sum all the elements of this
# vector.
# x =  2 −4 9 −8
#     −3 2 −1 0
#      5 4 −3 3
# ii. Compute the absolute value of x for all the rows and columns separately.
# iii. Compute the square of each elements of x.
# iv. Swap the first row by the second row.
# v. Replace the first row by zeros and the third row by ones.
# vi. Compute the mean and standard deviation of first and third row.
# vii. Sum all the columns and then sum the results.
# ----------------------------------------------------------------





# =================================================================
# E.6:
# Write a Python code to show a bar chart using famous languages.
# Languages: Java, Python, PHP, JavaScript, C#, C++
# Usage (Perecent): 22.2, 17.6, 8.8, 8, 7.7, 6.7
# ----------------------------------------------------------------





# =================================================================
# E.7:
# Write a Python code to create bar plots with errorbars on the same plot. Put labels above each
# bar displaying men average (integer value).
# Sample Date
# Average: 0.14, 0.32, 0.47, 0.38
# STD: 0.23, 0.32, 0.18, 0.46
# ----------------------------------------------------------------





# =================================================================
# E.8:
# Write a script to find the second largest number in an array (use random number generator) and
# multiply it by 50.
# ----------------------------------------------------------------

rand = np.random.randint(0,100,5)*50
sorted = np.sort(rand)

print(sorted)
print(sorted[-2])

