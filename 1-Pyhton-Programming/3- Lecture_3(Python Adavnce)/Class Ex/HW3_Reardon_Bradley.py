# =================================================================
# Class_Ex1:
# Writes a python script (use class) to simulate a Stopwatch .
# push a button to start the clock (call the start method), push a button
# to stop the clock (call the stop method), and then read the elapsed time
# (use the result of the elapsed method).
# ----------------------------------------------------------------
class stopwatch:
    def __init__(self, start, stop, reset):
        self.start = start
        self.stop = stop
        self.reset = reset
    def start(stopwatch):
    from time import clock
        return

def stop(stopwatch):
        from time import clock
    stop_time = clock(stopwatch)

class counting_stopwatch:
    def __init__


# use sleep to simulate the program to check it is working correctly



# =================================================================
# Class_Ex2:
# Write a python script (use class)to implement pow(x, n).
# ----------------------------------------------------------------

class pow:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def power(self):
        return self.x**self.n

n = pow(5, 3)
n.power()








# =================================================================
# Class_Ex3:
# Write a python class to calculate the area of rectangle by length
# and width and a method which will compute the area of a rectangle.
# ----------------------------------------------------------------

class area_of_rect:
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def calc(self):
        return self.l * self.w

area = area_of_rect(5, 10)
area.calc()





# =================================================================
# Class_Ex4:
# Write a python class and name it Circle to calculate the area of circle
# by a radius and two methods which will compute the area and the perimeter
# of a circle.
# ----------------------------------------------------------------

class Circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return self.r ** 2 * 3.14159265359

    def perimeter(self):
        return 2 * 3.14159265359 * self.r


circ = Circle(5)
area = circ.area()
perimeter = circ.perimeter()

print('Area: ' + str(area),'Perimeter: ' + str(perimeter))




# =================================================================
# E.1
# Write a script to find duplicates from an array (define an array with some duplicates on it). If
# you use built in function in python explain the methods and how this methods are working.
# ----------------------------------------------------------------

array = [1,2,2,3,3,3,4,5,5,5,5,6,6,6,1,'f','f']

def duplicates(x):
    z = []
    for i in range(len(x)):
        if x.count(x[i]) > 1:
            if x[i] not in z:
                z += [x[i]]
    print(z)

duplicates(array)

# The count() method returns an integer representing the number of times an input value exists in an object.

# =================================================================
# E.2:
# Write a script that finds all such numbers which are divisible by 2 and 5, less than 1000. If you
# use built in function in python explain the methods and how this methods are working.
# ----------------------------------------------------------------

def divis_by_five_or_two():
    for i in range(1,1000):
        if i % 2 == 0 and i % 5 == 0:
            print(i)
divis_by_five_or_two()




# =================================================================
# E.3:
# Write a Python class to convert a roman numeral to an integer. Hint: (Use the following symbols
# and numerals Wiki )
# ----------------------------------------------------------------

class roman:
    def rom_int(self, rom_num):
        dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        for i in range(len(rom_num)):
            if i > 0 and dict[rom_num[i]] > dict[rom_num[i-1]]:
                z += dict[rom_num[i]] - 2*dict[rom_num[i-1]]
            else:
                z += dict[rom_num[i]]
        print(z)

roman().rom_int('MMMCMLXXXVI')








# =================================================================
# E.4:
# Write a Python class to find sum the three elements of the given array to zero.
# Given: [-20, -10, -6, -4, 3, 4, 7, 10]
# Output : [[-10, 3, 7], [-6, -4, 10]]
# ----------------------------------------------------------------

class ten_sum:





