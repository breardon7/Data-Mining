# %% 1- Load the image.png into python and convert it to grey scale then print the data type.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q1" + 20* "-")
import matplotlib.pyplot as plt
import numpy as np


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])
orig = plt.imread('6103_image.png')

grey = rgb2gray(orig)

print(orig.shape)
print(grey.shape)

# %% 2- Plot the image and explain the features of the figure (color or black and white, size of the image, resolution)
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q2" + 20* "-")


plt.imshow(orig)
plt.show()

plt.imshow(grey)
plt.show()


# The figure returns as a colored image even after converting to greyscale, but the colors do not perfectly match the
# original image. The image was converted from a (512, 512, 4) array to a (512, 512) array, or from a 3d to a 2d array.
# The resolution is 512 x 512, or 262144 pixels.


# %% 3- Flip the image 90, 180, 270 degree by using numpy.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q3" + 20* "-")

rot90 = np.rot90(grey)
rot180 = np.rot90(rot90)
rot270 = np.rot90(rot180)
plt.imshow(rot90)
plt.show()
plt.imshow(rot180)
plt.show()

plt.imshow(rot270)
plt.show()

# %% 4- Remove the background and try to find the camera man in the picture (set the background to white or black)
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q4" + 20* "-")

green = orig[:,:,1]

for i in green:
    if i < .255:
        i = 0

print(orig)
plt.imshow(orig)
plt.show()



# %% 5- Keep the background and try color the cameraman by white colors.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q5" + 20* "-")
