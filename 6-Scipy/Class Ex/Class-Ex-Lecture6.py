# =================================================================
# Class_Ex1:
# We will do some  manipulations on numpy arrays by importing some
# images of a racoon.
# scipy provides a 2D array of this image
# Plot the grey scale image of the racoon by using matplotlib
# ----------------------------------------------------------------
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

face = misc.face(gray=True)  ## Modify the face function
print(face.shape)
plt.imshow(face)
plt.show()




print('#',50*"-")
# =================================================================
# Class_Ex2:
# If still the face is gray choose the color map function and make it
# gray
# ----------------------------------------------------------------

plt.gray()
plt.imshow(face)
plt.show()


print('#',50*"-")
# =================================================================
# Class_Ex3:
# Crop the image (an array of the image) with a narrower centering
# Plot the crop image again.
# ----------------------------------------------------------------

face1 = face
face1[0:200] = 255
face1[600:800] = 255
face1[:,:201] = 255
face1[:,800:] = 255
plt.imshow(face1)
plt.show()

print('#',50*"-")
# =================================================================
# Class_Ex4:
# Take the racoon face out and mask everything with black color.
# ----------------------------------------------------------------

face3 = misc.face(gray=True)
face3[175:325, 400:925] = 0
face3[325:375, 500:900] = 0
face3[375:425, 555:830] = 0
face3[425:475, 555:715] = 0
plt.imshow(face3)
plt.show()


print('#',50*"-")
# =================================================================
# Class_Ex5:
# For linear equation systems on the matrix form Ax=b where A is
# a matrix and x,b are vectors use scipy to solve the for x.
# Create any matrix A and B (Size matters)
# ----------------------------------------------------------------

from scipy import linalg
import numpy as np
a5 = np.random.randint(1, 25, 25).reshape(5, 5)
b5 = np.random.randint(1, 10, 5).reshape(5, 1)
print(linalg.solve(a5, b5))

print('#',50*"-")
# =================================================================
# Class_Ex6:
# Calculate eigenvalue of matrix A. (create any matrix and check your
# results.)
# ----------------------------------------------------------------

a6 = np.random.randint(1, 25, 25).reshape(5, 5)
print(linalg.eig(a6))

print('#',50*"-")
# =================================================================
# Class_Ex7:
# Sparse matrices are often useful in numerical simulations dealing
# with large datasets
# Convert sparse matrix to dense and vice versa
# ----------------------------------------------------------------









print('#',50*"-")

# =================================================================
# Class_Ex8:
# Create any polynomial to order of 3 and write python function for it
# then use scipy to minimize the function (use Scipy)
# ----------------------------------------------------------------











print('#',50*"-")
# =================================================================
# Class_Ex9:
# use the brent or fminbound functions for optimization and try again.
# (use Scipy)
# ----------------------------------------------------------------









print('#',50*"-")
# =================================================================
# Class_Ex10:
# Find a solution to a function. f(x)=0 use the fsolve (use Scipy)
# ----------------------------------------------------------------











print('#',50*"-")
# =================================================================
# Class_Ex11:
# Create a sine or cosine function with a big step size. Use scipy to
# interpolate between each data points. Use different interpolations.
# plot the results (use Scipy)
# ----------------------------------------------------------------










print('#',50*"-")
# =================================================================
# Class_Ex12:
# Use scipy statistics methods on randomly created array (use Scipy)
# PDF, CDF (CUMsum), Mean, Std, Histogram
# ----------------------------------------------------------------








print('#',50*"-")
# =================================================================
# Class_Ex13:
# USe hypothesise testing  if two datasets of (independent) random varibales
# comes from the same distribution (use Scipy)
# Calculate p values.
# ----------------------------------------------------------------






print('#',50*"-")
# ----------------------------------------------------------------