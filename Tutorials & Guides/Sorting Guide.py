from random import randint, shuffle
from math import log10, floor
from time import time


def MakeList(elements, Min=0, Max=99):  # Makes an unsorted list [0,99] of given size
    out = []
    for i in range(elements):
        out.append(randint(Min, Max))

    return out

'''
Bubble Sort simply goes through the list and picks two neighboring values.
It then puts these values in numerical order. For example, if it encounters
(23,7), it will swap these to (7,23).

Since some values can be more than one "space" out of place, the algorithm
must go through the list multiple times until every value is in the correct
correct position. Worst case, this will take (n-1)**2 swaps for a list of size n.
We disreguard everything except the highest degree and say that Bubble sort runs
in O(n**2) time, or has O(n**2) complexity.
'''


def BubbleSort(list):  # Works in O((n-1)^2) time
    changed = True
    while changed:
        changed = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                changed = True

    return list

'''
Insertion sort works by inserting unsorted elements of a list into the correct
position. Here's how it works. Let's say our unsorted list is (11,15,6,12):

1) Since 11<15, 11 stays where it is
    Our list is now (11,15,6,12)

2) Since 15>6, 15 is inserted in front of the 6
    Our list is now (11,6,15,12)

3) Since 11>6, 11 is inserted in front of the 6
    Our list is now (6,11,15,12)

4) Since 15>12, 15 is inserted in front of the 12
    Our list is now (6,11,12,15)

* Steps 2 and 3 are sort of the same step, but the code still has to
compare 

** Really our list looks something like (11,15,15,12) or (6,11,15,15),
after each swap, but the comparitor value will eventually replace one of
these repeated values, or the repeated value will change to another group.
For example, when our list is (11,11,15,12), our comparitor is 6.
When our list is (6,11,15,15), our comparitor is 12.
The comparitor value will always be this missing/repeated value

This algorithm works in O(n*ln(n)) time, faster than Bubble Sort.
For example, Insertion Sort will do about 93,000 swaps to sort a 10,000
element list while Bubble Sort will do 100,000,000
'''


def InsertionSort(l):
    for i in range(1, len(l)):
        j = i - 1
        comparitor = l[i]
        while(l[j] > comparitor) and j >= 0:
            l[j + 1] = l[j]     
            j -= 1
        l[j + 1] = comparitor
    return l    

'''
Most of the time, you can just use l.sort() to sort your list.
The built-in function uses somthing called Timsort, which runs in
O(n*ln(n)) complexity and O(n) space complexity -- pretty good
'''


# Helper function for Radix
def SortByDigit(arr, digit):
    out = []
    digit = int(log10(digit) + 1)
    digit = len(str(arr[0])) - digit
    a = 0
    for i1 in range(0, 11):
        for i2 in range(0, len(arr)):
            if str(arr[i2])[digit] == str(i1):
                out.append(arr[i2])
    return out

'''
Radix Sort works by sorting each digit in each number from ones up.
this sorting is usually faster than insertion sort because it has Linear time
complexity. It still does't really beat the built-in sort()function, even
if sort() has a higher time complexity. Radix sort works fastest with numbers
that are of of limited size, such as only three digits.
'''


# Precondition: All elements have the same number of digits
def Radix(arr):
    max1 = floor(log10(arr[0]) + 1)
    exp = 1
    
    while max1 / exp > 0:
        arrold = arr
        try: arr = SortByDigit(arr, exp)
        except IndexError: return arrold
        
        exp *= 10
        
    return arrold


for i in range(10):
    l = MakeList(10000, 1000, 9999)

    t1 = time()
    Radix(l)
    time1 = time() - t1
    
    t1 = time()
    InsertionSort(l)
    print(time1 - (time() - t1))
