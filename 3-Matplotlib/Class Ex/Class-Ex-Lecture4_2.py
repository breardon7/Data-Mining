# =================================================================
# Class_Ex1:
# Class_Ex1:
# Find the slope of the following curve for each of its points
#                  y = np.exp(-x ** 2)
# Then plot it with the original curve np.exp(-X ** 2) in the range
# (-3, 3) with 100 points in the range
# ----------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-3,3,100)
y1 = np.exp(-x1 ** 2)
plt.plot(x1, y1)
plt.show()


# =================================================================
# Class_Ex2:
# A file contains N columns of values, describing N–1 curves.
# The first column contains the  x coordinates, the second column
# contains the y coordinates of the first curve, the third
# column contains the y coordinates of the second curve, and so on.
#  We want to display those N–1 curves.
# ----------------------------------------------------------------

# rand100 = np.random.randint(1,100,250)
# reshaped100 = rand100.reshape(25, 10)
# print(reshaped100)

#x2 = np.linspace(0,6,100)
#xreshape = x2.reshape(100,1)
#y2 = np.exp(-x2**2).reshape(100,1)
#y3 = np.exp(x2**3).reshape(100,1)
#xplus = np.concatenate(xreshape, y2, y3)
#plt.plot(x2,y2)
#plt.plot(x2,y3)
#plt.show()



# =================================================================
# Class_Ex3: 
# Write a efficient code to stack any number of layers of data into
# a bar chart plot.
# Use the following data.
# ----------------------------------------------------------------
data = np.random.rand(5,3)
color_list = ['b', 'g', 'r', 'k', 'y']
x = np.arange(3)
bottom = np.cumsum(data, axis=0)

for i in x:
    if i == 0:
        plt.bar(x, data[i], color = color_list[i])
    else:
        plt.bar(x, data[i], color = color_list[i], bottom = bottom[i-1])
plt.show()



# =================================================================
# Class_Ex4:
# Write a Python code to plot couple of lines
# on same plot with suitable legends of each line.
# ----------------------------------------------------------------

x4 = np.linspace(0,10,20)
squared = x4**2
cubed = x4**3
plt.plot(x4, squared, label = 'x-squared')
plt.plot(x4, cubed, label = 'x-cubed')
plt.legend()
plt.show()





# =================================================================
# Class_Ex5:
# Write a Python code to plot two or more lines with legends,
# different widths and colors.
# ----------------------------------------------------------------

x5 = np.linspace(0, 20, 100)
y51 = x5*3 + 7
y52 = -x5**2 - 4

plt.plot(x5, y51, label = 'first', linewidth = .5, color = 'b')
plt.plot(x5, y52, label = 'second', linewidth = 4, color = 'y')
plt.legend()
plt.show()




# =================================================================
# Class_Ex6:
# Write a Python code to plot two or more lines and set the line markers.
# ----------------------------------------------------------------

x6 = np.linspace(0,10,20)
y61 = x6**2
y62 =-x6**3

plt.plot(x6, y61, label = 'o', marker = 'o', color = 'b')
plt.plot(x6, y62, label = '*', marker = '*', color = 'y')
plt.legend()
plt.show()





# =================================================================
# Class_Ex7:
# Write a Python code to show grid and draw line graph of
# revenue of certain compan between November 4, 2017 to November 4, 2018.
# Customized the grid lines with linestyle -, width .6. and color blue.
# ----------------------------------------------------------------

dates = ['4-11-2017', '4-11-2018']
y7 = [10394, 34003]
plt.plot(dates, y7, label = 'Revenue', c = 'r')
plt.legend()
plt.grid(True, c = 'b', lw = .6, ls = '-')
plt.title('Revenue History for Company X')
plt.show()


# =================================================================
# Class_Ex8:
# Write a Python code to create multiple empty plots  in one plot
# (facets)
# ----------------------------------------------------------------

plt.subplots(nrows = 3, ncols=2,)
plt.show()






