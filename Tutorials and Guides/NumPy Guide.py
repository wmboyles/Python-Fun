'''
WHAT IS NUMPY?

NumPy is a popular Python library for efficiently working multidimensional 
arrays (vectors and matrices). It's written in C, so you can get the 
performance benefits while still being able to write simple Python.
Often, NumPy arrays take less memory than pure Python ones.

INSTALL
You can install it on your own system using pip or Conda.
You can also build it from source if you really want.
    pip/pip3: pip install numpy
    Conda: Conda install numpy
'''

# Normal way to import numpy
import numpy as np

# Some other useful stuff for demos
import time
import sys

BIG_LIST_SIZE = 100**2


'''
MEMORY COMPARISON

We'll make a list (technically a range) of the numbers 0 to 9999 in both Numpy 
and Python and compare the number of bytes each ones takes in memory.
'''
python_range = range(BIG_LIST_SIZE)
print(type(python_range), "size:", sys.getsizeof(python_range)*len(python_range))

numpy_range = np.arange(BIG_LIST_SIZE) # This is one way to make an array
print(type(numpy_range), "size:", numpy_range.size*numpy_range.itemsize)

'''
SPEED COMPARISON

We'll make two ranges in Python and two arrays in NumPy and see how long it
takes to make a new object that is the sum of the elements of the two lists.

[1,2,3,4,5] + [1,2,3,4,5] = [2,4,6,8,10]
'''
# Python lists
python_r1 = range(BIG_LIST_SIZE)
python_r2 = range(BIG_LIST_SIZE)

# time it
start = time.time()
python_result = [(x+y) for x,y in zip(python_r1, python_r2)] # Do the operation
end = time.time()
print("Python range took", (end-start)*1000, "ms")

# NumPy lists
numpy_r1 = np.arange(BIG_LIST_SIZE)
numpy_r2 = np.arange(BIG_LIST_SIZE)

start = time.time()
numpy_result = numpy_r1 + numpy_r2
end = time.time()
print("NumPy took", (end-start)*1000, "ms")

'''
MAKING ARRAYS

We can declare a NumPy array lots of ways
'''

# As a range
a = np.arange(1,100,2)

# As a Multi-dimensonal aray
arr = [[5,6,5],[1,6,3],[3,6,2]]
a=np.array(arr)

# Using different datatypes
a = np.array([[5,6,5],[1,6,3],[3,6,2]], dtype=np.float)
#DATA TYPES ARE: bool, int, float, and complex. Many of these can have a specified data size (ie int8) or be unsigned (ie uint8).

# As all 0's or all 1's
a = np.zeros((3,4))
a = np.ones((4,5))

# an "empty" array
a = np.empty((2,3))

# As some special types of lin alg matrices
a = np.identity(5)

# A number of elements
l = np.linspace(0, 2*np.pi, 100) #0, 2pi/100, 2*2pi/100, ...

# A random matrix
rand = np.random.rand(3,2) # Values over [0,1)


'''
SIMPLE OPERATIONS

Let's do some simple NumPy array operations.
'''
a = np.array([[6,48,2000],[97,0,62],[8,24,8]]) # Another way to make an array

# Dimensions
print("Array Dimension:", a.ndim)

# Size of each element in bytes
print("Element Byte Size:", a.itemsize)
# Really big numbers need more space, but 4 bytes is usually enough

# Print out the array nice and pretty
print(a)

# Numner of elements in the array
print("Number of elements:", a.size)

# Height and width (and other dimensions if they exist)
print("(height, width):", a.shape)

# Adding / Substracting
a_doubled = a + a # or np.add(a,a)
zero_a = a - a

# Multiplying or dividing by a scalar
a_halfed = a / 2 # or a /= 2
a_doubled = a * 2 # or a *= 2

# Reshape
a = np.arange(BIG_LIST_SIZE)
a = np.reshape(a, (100,100)) # or a.shape = 100,100

# Transpose (swap rows and cols)
b = a.T

# Multiplying two matrices
a_squared = a @ a

# Applying a function to each element
a = np.sin(l)
# sin, cos, exp, sqrt, and floor are most common

# Making a deep copy
a_copy = a.copy()

# Making a new refernce to the same object
a_ref = a

# Dot product of two vectors
v1 = np.array([5,-2,3])
v2 = np.array([-2,7,1])
v_dot = v1.dot(v2)
print(v_dot)
v_cross = np.cross(v1, v2)
print(v_cross)

# Basic linalg
a = np.array([[3,1],[1,2]])
b = np.array([9,8])
x = np.linalg.solve(a,b)    # 3x + 1y = 9
                            # 1x + 2y = 8
# x = 2, y = 3

a = np.array([[1.0, 2.0], [3.0, 4.0]])
a.transpose()
np.linalg.inv(a)

'''
NUMPY WITH OTHER LIBRARIES

Numpy is most often used with other libraries, like matplotlib or OpenCV.
'''
# Making a histogram in matplotlib
import matplotlib
matplotlib.use("TkAgg") # For some reason conda uses a non-gui backend by default
import matplotlib.pyplot as plt

mu, sigma = 2, 0.5 # Mean 2, variance 0.5^2
v = np.random.normal(mu,sigma,BIG_LIST_SIZE*100) # nromally distributed lots of times
plt.hist(v, bins=50, normed=1)
#plt.show()

# Turning an image to black and white using OpenCV
import cv2
im = cv2.imread("me.jpg")
im = cv2.resize(im, (720, 480))
print("Image Type:", type(im))
cv2.imshow("Color Image", im)
gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
cv2.imshow("Gray Image", gray)

while True:
    if cv2.waitKey(1) == 27: 
        cv2.destroyAllWindows()
        break
