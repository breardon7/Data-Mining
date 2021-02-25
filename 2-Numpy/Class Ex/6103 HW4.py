# =================================================================
# E.1:
# Write a script to
# i. Sum all the items in a array (use random number generator and multiply it by 100, create a
# vector with the size 200).
# ii. Get the largest number and smallest number with the indexing of it.
# iii. plot the following vector and check your min and max value that you find in section i.
# ----------------------------------------------------------------
print('-'*50+'Q1'+'-'*50)
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
hundred = np.random.randint(50, 100, 200) * 100
hr = hundred.reshape(100,2)
sorted_hund = np.sort(hundred)
sum_hund = sum(hundred)
largest = sorted_hund[-1]
smallest = sorted_hund[0]
v = np.array([smallest, largest])
origin = np.array([[0, 0], [0, 0]])
plt.quiver(*origin, v[0], v[1], scale = 1)
plt.xlim (-10, v[0]+1)
plt.ylim(-10, v[1]+1)
plt.show()


# =================================================================
# E.2:
# Plot the following functions x, sin(x), e**x
# and log(x) over the interval 1 < x < 6 with the step
# size of 0.1. (Put the title x axis label and y axis label for each plot)
# ----------------------------------------------------------------
print('-'*50+'Q2'+'-'*50)
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
print('-'*50+'Q3'+'-'*50)
vector_x = np.random.normal(loc = 0, scale = 1, size = 1000)
vector_y = np.random.uniform(low = 0, high = 1, size = 1000)
xm = np.mean(vector_x)
ym = np.mean(vector_y)
xst = np.std(vector_x)
yst = np.std(vector_y)
plt.hist(vector_x, 35)
plt.xlabel('Normal Distribution')
plt.ylabel('Freguency')
plt.title('Frequency of Normally Distributed Values')
plt.show()
plt.hist(vector_y, 35)
plt.xlabel('Uniform Distribution')
plt.ylabel('Freguency')
plt.title('Frequency of Uniformly Distributed Values')
plt.show()

# The gaussian histogram shows that x is a normally distributed population.
# The  uniform histogram shows that y is a uniformly distributed population.
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
print('-'*50+'Q4'+'-'*50)
A = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
print(A)
x4 = A[:,0]
y4 = A[:,-2:-1]
s4 = x4+np.sum(A[1,:])
np.linalg.norm(x4)
A1 = A[:,[0,1,2]] = A[:,[1,0,2]]
A1 = A1[[0,2], :]
print(A1)


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
print('-'*50+'Q5'+'-'*50)

sqsum = sum(np.arange(20,35)**2)

x5 = np.array([2, -4, 9, -8, -3, 2, -1, 0, 5, 4, -3, 3]).reshape(3,4)
x5_abs = abs(x5)
x5_sq = x5**2
x5[[0,1]] = x5[[1,0]]
x5[0] = 0
x5[2] = 1
x5_means_rows_1_3 = np.mean(x5[0]), np.mean(x5[2])
x5_stds_rows_1_3 = np.std(x5[0]), np.std(x5[2])
x5_col_sums = np.sum(x5, axis=1)
x5_sum_of_col = np.sum(x5_col_sums)

#x5 = np.array([2, −4, 9, −8,−3, 2, −1, 0,5, 4, −3, 3]).reshape(3,3)


# =================================================================
# E.6:
# Write a Python code to show a bar chart using famous languages.
# Languages: Java, Python, PHP, JavaScript, C#, C++
# Usage (Perecent): 22.2, 17.6, 8.8, 8, 7.7, 6.7
# ----------------------------------------------------------------
print('-'*50+'Q6'+'-'*50)

languages = np.array(['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'])
usage = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
sns.barplot(languages, usage)
plt.xlabel('Languages')
plt.ylabel('Percentage of Usage')
plt.title("Percentage of Language Usage")
plt.show()



# =================================================================
# E.7:
# Write a Python code to create bar plots with errorbars on the same plot. Put labels above each
# bar displaying men average (integer value).
# Sample Date
# Average: 0.14, 0.32, 0.47, 0.38
# STD: 0.23, 0.32, 0.18, 0.46
# ----------------------------------------------------------------
print('-'*50+'Q7'+'-'*50)

average = np.array([0.14, 0.32, 0.47, 0.38])
groups = np.array([1,2,3,4])
std = np.array([0.23, 0.32, 0.18, 0.46])
bar = sns.barplot(x = groups, y = average, yerr = std)
for i in range(len(average)):
    bar.text(x = groups[i]-1, y = average[i], s = average[i])
plt.show()


# =================================================================
# E.8:
# Write a script to find the second largest number in an array (use random number generator) and
# multiply it by 50.
# ----------------------------------------------------------------
print('-'*50+'Q8'+'-'*50)

rand = np.random.randint(0, 100, 5)
sorted = np.sort(rand)
print(sorted)
print(sorted[-2] * 50)

