import numpy as np
import time
import sys

'''
HOW TO MAKE A NUMPY ARRAY VS PYTHON LIST & MEMORY COMPARISON

list_x = range(1000) #1000 element python list (integers)
print(sys.getsizeof(5)*len(list_x)) #get #of bytes of list

array_np = np.arange(1000) #1000 element numpy array (integers)
print(array_np.size*array_np.itemsize) #get #of bytes of numpy array
'''


'''
NUMPY ARRAY SPEED DEMO

SIZE = 1000000

L1 = range(SIZE) #1000 element python List (integers)
L2 = range(SIZE) #see above

a1 = np.arange(SIZE) #1000 element numpy array (integers)
a2 = np.arange(SIZE) #see above

start = time.time() #record start time
result = [(x+y) for x,y in zip(L1,L2)] #add elements from list
print("List took: ",(time.time()-start)*1000,"ms to add ",SIZE," elements.") #record time taken

start = time.time() #reset start time
result = a1+a2 #add array elements (much simplier than lists)
#add array elements
print("Array took: ",(time.time()-start)*1000,"ms to add ",SIZE," elements.") #record time taken
'''
'''
a=np.array([[5,6,5],[1,6,3],[3,6,2]]) #3x3 2D NumPy Array

print("Array Dimension: ",a.ndim) #print array dimension (2D)

print("Element Byte Size: ",a.itemsize) #print byte size of each element (the byte size of the largest entry)
    #Note that large numbers (like 5928359234) and floats take 8 bytes while smaller integers take 4 bytes

print(a) #print the array (is formatted)

print("Number of elements: ",a.size) #print number of array elements

print("Array Size (height,width): ",a.shape) #print array dimensions (this is not a tuple)

a2 = np.array([[5,6,5],[1,6,3],[3,6,2]], dtype=complex) #arrays can have a specified data type
    #DATA TYPES ARE: bool, int, float, and complex. Many of these can have a specified data size (ie int8) or be unsigned (ie uint8).
print(a2)

a3 = np.zeros((3,4)) #arrays of a specified size can be created with placeholder values
    #The placeholder values that have np.### for them are ONLY np.zeros and np.ones
print(a3)


a4 = np.arange(1,10,2) #creates array with elements from 1 to 9 by steps of 2 (1,3,5,7,9)
print(a4)
'''

