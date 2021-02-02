# Class_Ex1:
# Write python program that converts seconds to
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------
print('Enter a given number of seconds to convert seconds to hours and minutes:')
s = eval(input())
hours = int(s/3600)
mins = int((s - 3600*hours)/60)
secs = int(s - 3600*hours - 60*mins)
print(str(s) + ' seconds is equal to ' + str(hours) +' hours, ' + str(mins) + ' mins, and ' + str(secs) + ' seconds.')






# =================================================================
# Class_Ex2:
# Write a python program to print all the different arrangements of the
# letters A, B, and C. Each string printed is a permutation of ABC.
# ----------------------------------------------------------------
print('All permutations of ABC:')
for i in 'ABC':
    first_term = i
    for j in 'ABC':
        second_term = j
        if i != j:
            for k in 'ABC':
                third_term = k
                if j != k and i!=k:
                    print(i+j+k)




# =================================================================
# Class_Ex3:
# Write a python program to print all the different arrangements of the
# letters A, B, C and D. Each string printed is a permutation of ABCD.
# ----------------------------------------------------------------

print('All permutations of ABCD:')
for i in 'ABCD':
    first_term = i
    for j in 'ABCD':
        second_term = j
        if i != j:
            for k in 'ABCD':
                third_term = k
                if j != k and i!=k:
                    for n in 'ABCD':
                        if j != k and i!=k and n!=k and j!=n and i!=n:
                            print(i+j+k+n)



# =================================================================
# Class_Ex4:
# Suppose we wish to draw a triangular tree, and its height is provided
# by the user.
# ----------------------------------------------------------------
print("Input an integer for the triangular tree's height: ")

h = eval(input())
star = '* '
space = ' '
for i in range(0,h+1):
   print(space*((h-i))+star*i)





# =================================================================
# Class_Ex5:
# Write python program to print prime numbers up to a specified values.
# ----------------------------------------------------------------
print('Input an integer to find all prime numbers up to and including that integer: ')
x = eval(input())

for i in range(1, x + 1):
   if i > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
           print(i)






# =================================================================
