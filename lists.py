"""
    def binarySearch(self, target): #This implementation may be better for arrays, where all accesses are O(1)
        if self.__size == 0: return -1
        else: return self.__binarySearch2(target, 0, self.__size - 1)

    def __binarySearch2(self, target, minIdx, maxIdx): #This implementation may be better for arrays, where all accesses are O(1)
        if minIdx > maxIdx: return -(minIdx + 1)
        midIdx = (minIdx + maxIdx)//2
        val = self.get(midIdx)
        if val == target: return midIdx
        elif val < target: return self.__binarySearch2(target, midIdx + 1, maxIdx)
        elif val > target: return self.__binarySearch2(target, minIdx, midIdx - 1)
"""
import unittest
from numpy.ma.testutils import assert_equal
from _operator import index
from pip._internal.utils.outdated import SELFCHECK_DATE_FMT


class arrayList:
    """
    Although this class is somewhat redundant in Python because lists naturally grow and shrink,
    but it's good practice. Elements can be added or removed in any order. Data is stored in a
    list, allowing an access at any index to be O(1). Duplicate and null (None) elements are
    allowed. One can iterate through this list using for-in loops. Due to Python beging a
    dynamically typed language, elements of any type can be in the list.
    """

    def __init__(self):
        """
        Constructs a new, empty array list of size 0.
        """
        
        self.__l = []
        self.__size = 0

    def size(self):
        """
        Returns the size of the list, which is the number of elements within.
        """
        
        return self.__size

    def isEmpty(self): 
        """
        Answers the question: Does the list have 0 elements?
        """
        
        return self.__size == 0

    def contains(self, value):
        """
        Answers the question: Does the list contain this value?

        Note: this can be accomplished faster with binary search.
        """
        
        for e in self.__l:
            if e == value: return True

        return False
    
    def isSorted(self):
        """
        Answers the question: is the list in sorted order?
        """
        
        if self.__size <= 1: return True
        
        prev = self.__l[0]
        for i in range(1, len(self.__l)):
            val = self.__l[i]
            if prev > val: return False
            
            prev = val
            
        return True
    
    def sort(self):
        """
        Puts this list into low to high sorted order.
        """
        
        self.__l = self.__mergeSort(self.__l)
    
    def __mergeSort(self, l):
        """
        Uses merge sort to put this list into sorted order.
        """
        
        if len(l) <= 1: return l
        
        # Split
        mid = len(l) // 2
        l1 = self.__mergeSort(l[:mid])
        l2 = self.__mergeSort(l[mid:])
        
        # Merge
        merged = []
        i1 = 0
        i2 = 0
        for i in range(len(l1) + len(l2)):
            if i2 == len(l2) or (i1 < len(l1) and l1[i1] <= l2[i2]):
                merged.append(l1[i1])
                i1 += 1
            else:
                merged.append(l2[i2])
                i2 += 1
                
        return merged

    def indexOf(self, value):
        """
        Returns the index of the specified value in the list. If this value is not end the list,
        this function returns -1.
        """
        
        for i in range(self.__size):
            if self.__l[i] == value: return i

        return -1

    def set(self, index, value):
        """
        Sets an element at a specified index to a specified value and returns the value
        previously at the specified index. If the index parameter is outside the range of the
        list, this function raises an Exception.
        """
        
        if index < 0 or index >= self.__size: raise Exception
        
        ret = self.__l[index]
        self.__[index] = value
        return ret

    def get(self, index):
        """
        Returns the element at a spefified index in the list. If the index parameter is outside
        the range of the list, this function raises an Exception.
        """
        
        if index < 0 or index >= self.__size: raise Exception
        
        return self.__l[index]

    def add(self, value, index=None):
        """
        Adds a specified value at optionally a specified index, incrementing the list's size.
        If no index field is given, the value is added to the end of the list. Also, this
        function will return True if no index parameter is given, and the value parameter is
        successfully added to the list. If the index parameter is outside the range of the list,
        this function raises an Exception.
        """
        
        returnTrue = False
        if index is None:
            index = self.__size
            returnTrue = True
        elif index < 0 or index > self.__size: raise Exception

        # Create empty spot
        self.__l.append(None)
        
        # right-shift elements
        for i in range(self.__size, index - 1, -1): self.__l[i] = self.__l[i - 1]
            
        self.__l[index] = value
        self.__size += 1

        if returnTrue: return True

    def addAll(self, iterable):
        """
        Adds all elements of an iterable object to the list. Elements returned earlier by the
        iterable's call to next() will be added to earlier positions in the list. If the
        iterable parameter is not in fact iterable, this function raises an Exception.
        """
        
        try:
            for item in iterable: self.add(item)
        except TypeError as te: raise Exception

    def remove(self, index=None):
        """
        Removes an element from an optionally specified index, decrementing the list's size.
        This function returns the removed value. If no index parameter is specified, the last
        element in the list is removed and returned. If the index parameter is outside the range
        of the list, this function raises an Exception.
        """
        if index is None: index = self.__size - 1
        elif index < 0 or index >= self.__size: raise Exception

        # remove element
        ret = self.__l[index]
        self.__l[index] = None
        # left-shift elements
        for i in range(index, self.__size - 1): self.__l[i] = self.__l[i + 1]

        self.__size -= 1
        return ret

    def toString(self):
        """
        Returns a string representation of the list, which is a comma-separated list of values.
        """
        
        return ', '.join(str(s) for s in self.__l)

    def clear(self):
        """
        Empties all elements from the list, resetting the size to 0.
        """
        
        self.__l = None
        self.__size = 0

    def __iter__(self):
        """
        Returns an iterator that allows this list to be used in for-in loops. It does so by
        creating an idea of a current index, which starts at 0.
        """
        
        self.__currentIdx = 0
        return self

    def __next__(self):
        """
        Using fields created by the iter() function, this function returns the next value in the
        list from the current index, and advances the current index by 1 element.
        """
        
        if self.__currentIdx >= self.__size: raise StopIteration
        ret = self.__l[self.__currentIdx]
        self.__currentIdx += 1
        return ret
    

class linkedList:
    """
    A linked list is a linear data structure composed of nodes, where each node contains a piece of data
    and a reference to the next node in the list. A reference to the front of the list is maintained in
    linked list, along with the size. Due to the one-way nature of the connection between nodes, accessing
    an element is O(n). Due to Python being dynamically typed, elements of any type can be in the list.
    """

    def __init__(self):
        """
        Creates a new Linked List with an None front reference and 0 size.
        """
        
        self.__front = None
        self.__size = 0

    def size(self):
        """
        Returns the size of the list, which is the number of elements within.
        """
         
        return self.__size

    def isEmpty(self):
        """
        Answers the question: Does the list have 0 elements?
        """
         
        return self.__size == 0

    def contains(self, value):
        """
        Answers the question: Does the list contain this value? This function is part of a
        recursive pair with a private function.
        """
         
        return self.__contains(value, self.__front)

    def __contains(self, value, head):
        """
        This function is part of a recursive pair with a public function.
        """
        
        if head is None: return False
        if head.data == value: return True
        else: return self.__contains(value, head.next)
        
    def isSorted(self):
        """
        Answers the question: is the list in sorted order?
        """
        if self.__size <= 1: return True
        
        prev = self.__front
        current = prev.next
        
        for i in range(self.__size - 1):
            if prev.data > current.data: return False
            
            prev = current
            current = current.next
            
        return True
            
    def sort(self):
         """
         Puts the list into low-to-high sorted order.
         """   
         
         raise Exception("TODO") 

    def indexOf(self, value):
        """
        Returns the index of the specified value in the list. If this value is not end the list,
        this function returns -1.
        """
        
        current = self.__front
        for i in range(self.__size):
            if current.data == value: return i
            current = current.next
        return -1

        ret = self.__l[index]
        self.__[index] = value
        return ret

    def get(self, index):
        """
        Returns the element at a specified index in the list. If the index parameter is outside
        the range of the list, this function raises an Exception.
        """
        
        if index < 0 or index >= self.__size: raise Exception("Index out of bounds")
        
        current = self.__front
        for i in range(index): current = current.next
        return current.data

    def set(self, index, value):
        """
        Sets an element at a specified index to a specified value and returns the value
        previously at the specified index. If the index parameter is outside the range of the
        list, this function raises an Exception.
        """
        
        if index < 0 or index >= self.__size: Exception

        current = self.__front
        for i in range(index): current = current.next

        toRet = current.data
        current.data = value
        return toRet

    def add(self, value, index=None):
        """
        If the index parameter is outside the range of the list, this function raises an
        Exception.
        """
        
        returnTrue = False
        
        if index is None:
            index = self.__size
            returnTrue = True
            
        self.__add(index, value, 0, self.__front)
        self.__size += 1
        if returnTrue: return True

    def __add(self, idx, value, currIdx, head):
        """
        This function is part of a recursive pair with a private function.
        """
        
        if idx == 0: self.__front = self.Node(value, self.__front)
        elif self.__front is None: raise Exception
        elif currIdx + 1 == idx: head.next = self.Node(value, head.next)
        else: self.__add(idx, value, currIdx + 1, head.next)

    def addAll(self, iterable):
        """
        Adds all elements of an iterable object to the list. Elements returned earlier by the
        iterable's call to next() will be added to earlier positions in the list. If the
        iterable parameter is not in fact iterable, this function raises an Exception.
        """
        
        try:
            for item in iterable: self.add(item)
        except TypeError as te: raise Exception

    def remove(self, index=None):
        """
        If the index parameter is outside the range of the list, this function raises an
        Exception.
        """
        
        if index is None: index = self.__size - 1
        
        if index < 0 or index >= self.__size: raise Exception

        toRet = self.get(index)

        if index == 0:
            self.__front = self.__front.next
            self.__size -= 1
            return toRet

        current = self.__front
        for i in range(index - 1): current = current.next

        current.next = current.next.next
        self.__size -= 1
        return toRet

    def toString(self):
        """
        Returns a string representation of the list, which is a comma-separated list of values.
        This function is part of a recursive pair with a private function.
        """
        
        if self.__front is None: return ""
        else: return self.__toString(self.__front)

    def __toString(self, head):
        """
        This function is part of a recursive pair with a public function.
        """
        
        if head.next is None: return str(head.data)
        else: return str(head.data) + ", " + self.__toString(head.next)

    def clear(self):
        """
        Empties all elements from the list, resetting the size to 0.
        """
        
        self.__front = None
        self.__size = 0

    def __iter__(self):
        """
        Returns an iterator that allows this list to be used in for-in loops. It does so by
        creating an idea of a current index, which starts at 0.
        """
        
        self.__current = self.__front
        return self

    def __next__(self):
        """
        Using fields created by the iter() function, the function returns the next value in the
        list from the current index, and advances the current index by 1 element.
        """
        
        if self.__current is None: raise StopIteration
        ret = self.__current.data
        self.__current = self.__current.next
        return ret

    class Node:
        """
        A Node is the smallest element of a linked list. It contains a piece of data and a reference to
        the next Node in the list.
        """

        def __init__(self, data, next=None):
            """
            Creates a new Node with a given data value and optional next Node.
            """
            
            self.data = data
            self.next = next
        
    
class Test(unittest.TestCase):
    RUN = 0
    
    def setUp(self):
        self.ll = linkedList()
        self.al = arrayList()
    
    def testLists(self):
        self.assertEqual(0, self.ll.size())
        self.assertEqual(0, self.al.size())
        
    def testSize(self):
        self.assertEqual(0, self.ll.size())
        
        self.assertEqual(0, self.al.size())
        
        # Add single item [0]
        self.ll.add(0)
        self.al.add(0)
        
        self.assertEqual(1, self.ll.size())
        self.assertEqual(1, self.al.size())
        
        # Add multiple items [0,1,2,3,4]
        self.ll.addAll([1, 2, 3, 4])
        self.al.addAll([1, 2, 3, 4])
        
        self.assertEquals(5, self.ll.size())
        self.assertEquals(5, self.ll.size())
        
        # Add at index [0,1,2,3,-1,4]
        self.ll.add(-1, 3)
        self.assertEquals(-1, self.ll.get(3))
        self.assertEquals(6, self.ll.size())
        self.assertEquals(6, self.ll.size())
        
        self.al.add(-1, 3)
        self.assertEquals(-1, self.al.get(3))
        self.assertEquals(6, self.al.size())
        self.assertEquals(6, self.al.size())
        
        # Remove
        self.assertEquals(4, self.ll.get(self.ll.size() - 1))
        self.assertEquals(4, self.ll.remove())
        self.assertEquals(5, self.ll.size())

        self.assertEquals(4, self.al.get(self.al.size() - 1))
        self.assertEqual(4, self.al.remove())
        self.assertEquals(5, self.al.size())
        
        # Remove at index
        self.assertEquals(1, self.ll.remove(1))
        self.assertEquals(4, self.ll.size())
        
        self.assertEquals(1, self.al.remove(1))
        self.assertEquals(4, self.al.size())
        
    def testIsEmpty(self):
        #Empty
        self.assertTrue(self.ll.isEmpty())
        self.assertTrue(self.al.isEmpty())
        
        #Add element
        self.ll.add(0)
        self.al.add(0)
        self.assertFalse(self.ll.isEmpty())
        self.assertFalse(self.al.isEmpty())
        
        #Remove element
        self.assertEquals(0, self.ll.remove())
        self.assertEquals(0, self.al.remove())
        self.assertTrue(self.ll.isEmpty())
        self.assertTrue(self.al.isEmpty())

    def testContains(self):
        #Empty
        self.assertFalse(self.ll.contains(0))
        self.assertFalse(self.al.contains(0))
        self.assertFalse(self.ll.contains(1))
        self.assertFalse(self.al.contains(1))
        
        #Add element
        self.ll.add(0)
        self.al.add(0)
        self.assertTrue(self.ll.contains(0))
        self.assertTrue(self.al.contains(0))
        self.assertFalse(self.ll.contains(1))
        self.assertFalse(self.al.contains(1))
        
        #Add element 2
        self.ll.add(1, 1)
        self.al.add(1, 1)
        self.assertTrue(self.ll.contains(0))
        self.assertTrue(self.al.contains(0))
        self.assertTrue(self.ll.contains(1))
        self.assertTrue(self.al.contains(1))

    def testIsSorted(self):
        #Empty list
        self.assertTrue(self.ll.isSorted())
        self.assertTrue(self.al.isSorted())
        
        #Only one element
        self.ll.add(0)
        self.al.add(0)
        self.assertTrue(self.ll.isSorted())
        self.assertTrue(self.al.isSorted())
        
        #multiple sorted
        self.ll.add(1)
        self.al.add(1)
        self.assertTrue(self.ll.isSorted())
        self.assertTrue(self.al.isSorted())
        
        #multiple unsorted
        self.ll.add(-1, 2)
        self.al.add(-1, 2)
        self.assertFalse(self.ll.isSorted())
        self.assertFalse(self.al.isSorted())

    def testSort(self):
        self.ll.addAll([5,4,3,2,1])
        self.al.addAll([5,4,3,2,1])
        
        self.assertFalse(self.ll.isSorted())
        self.assertFalse(self.al.isSorted())
        
        #self.ll.sort()
        self.al.sort()
        #self.assertTrue(self.ll.isSorted())
        self.assertTrue(self.al.isSorted())

    def testIndexOf(self):
        self.fail("Not yet implemented")

    def testGet(self):
        self.fail("Not yet implemented")

    def testSet(self):
        self.fail("Not yet implemented")

    def testAdd(self):
        self.fail("Not yet implemented")

    def testAddAll(self):
        self.fail("Not yet implemented")

    def testRemove(self):
        self.fail("Not yet implemented")

    def testToString(self):
        self.fail("Not yet implemented")

    def testClear(self):
        self.fail("Not yet implemented")

    def testIterNext(self):
        self.fail("Not yet implemented")
