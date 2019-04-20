'''
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
'''

'''
Although this class is somewhat redundant in Python because lists naturally grow and shrink,
but it's good practice. Elements can be added or removed in any order. Data is stored in a
list, allowing an access at any index to be O(1). Duplicate and null (None) elements are
allowed. One can iterate through this list using for-in loops. Due to Python beging a
dynamically typed language, elements of any type can be in the list.
'''


class arrayList:
    '''
    Constructs a new, empty array list of size 0.
    '''

    def __init__(self):
        self.__l = []
        self.__size = 0

    '''
    Returns the size of the list, which is the number of elements within.
    '''

    def size(self): return self.__size

    '''
    Answers the question: Does the list have 0 elements?
    '''

    def isEmpty(self): return self.__size == 0

    '''
    Answers the question: Does the list contain this value?

    Note: this can be accomplished faster with binary search.
    '''

    def contains(self, value):
        for e in self.__l:
            if e == value: return True

        return False

    '''
    Returns the index of the specified value in the list. If ths value is not end the list,
    this function returns -1.
    '''

    def indexOf(self, value):
        for i in range(self.__size):
            if self.__l[i] == value: return i

        return -1

    '''
    Sets an element at a specicied index to a specified value and returns the value
    previously at the specified index. If the index parameter is outside the range of the
    list, this function raises an Exception.
    '''

    def set(self, index, value):
        if index < 0 or index >= self.__size: raise Exception
        
        ret = self.__l[index]
        self.__[index] = value
        return ret

    '''
    Returns the element at a spefified index in the list. If the index parameter is outside
    the range of the list, this function raises an Exception.
    '''

    def get(self, index):
        if index < 0 or index >= self.__size: raise Exception
        
        return self.__l[index]

    '''
    Adds a specified value at optionally a specified index, incrementing the list's size.
    If no index field is given, the value is added to the end of the list. Also, this
    function will return True if no index parameter is given, and the value parameter is
    successfully added to the list. If the index parameter is outside the range of the list,
    this function raises an Exception.
    '''

    def add(self, value, index=None):
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

    '''
    Adds all elements of an iterable object to the list. Elements returned earlier by the
    iterable's call to next() will be added to earlier positions in the list. If the
    iterable parameter is not in fact iterable, this function raises an Exception.
    '''

    def addAll(self, iterable):
        try:
            for item in iterable: self.add(item)
        except TypeError as te: raise Exception

    '''
    Removes an element from an optionally specified index, derementing the list's size.
    This function returns the removed value. If no index parameter is specified, the last
    element in the list is removed and returned. If the index parameter is outside the range
    of the list, this function raises an Exception.
    '''

    def remove(self, index=None):
        if index is None: index = self.__size - 1
        elif index < 0 or index >= self.__size: raise Exception

        # remove element
        self.__l[index] = None
        # left-shift elements
        for i in range(index, self.__size - 1): self.__l[i] = self.__l[i + 1]

        self.__size -= 1
        self.__l.pop()
        return self.__l.pop()

    '''
    Returns a string representation of the list, which is a comma-seperated list of values.
    '''

    def toString(self):
        return ', '.join(str(s) for s in self.__l)

    '''
    Empties all elements from the list, resetting the size to 0.
    '''

    def clear(self):
        self.__l = None
        self.__size = 0

    '''
    Returns an iterator that allows this list to be used in for-in loops. It does so by
    creating an idea of a current index, which starts at 0.
    '''

    def __iter__(self):
        self.__currentIdx = 0
        return self

    '''
    Using fields crated by the iter() function, the function returns the next value in the
    list from the current index, and advances the current index by 1 element.
    '''

    def __next__(self):
        if self.__currentIdx >= self.__size: raise StopIteration
        ret = self.__l[self.__currentIdx]
        self.__currentIdx += 1
        return ret
        
'''
A linked list is a linear data structure composed of nodes, where each node contains a piece of data
and a reference to the next node in the list. A reference to the front of the list is maintained in
linked list, along with the size. Due to the one-way nature of the connection between nodes, accessing
an element is O(n). Due to Python beging dynamically typed, elements of any type can be in the list.
'''


class linkedList:

    def __init__(self):
        self.__front = None
        self.__size = 0

    '''
    Returns the size of the list, which is the number of elements within.
    '''

    def size(self): return self.__size

    '''
    Answers the question: Does the list have 0 elements?
    '''

    def isEmpty(self): return self.__size == 0

    '''
    Answers the question: Does the list contain this value? This function is part of a
    recursive pair with a private function.
    '''

    def contains(self, value): return self.__contains(value, self.__front)

    '''
    This function is part of a recursive pair with a public function.
    '''

    def __contains(self, value, head):
        if head is None: return False
        if head.data == value: return True
        else: return self.__contains(value, head.next)

    '''
    Returns the index of the specified value in the list. If ths value is not end the list,
    this function returns -1.
    '''

    def indexOf(self, value):
        current = self.__front
        for i in range(self.__size):
            if current.data == value: return i
            current = current.next
        return -1

        ret = self.__l[index]
        self.__[index] = value
        return ret

    '''
    Returns the element at a spefified index in the list. If the index parameter is outside
    the range of the list, this function raises an Exception.
    '''

    def get(self, index):
        if index < 0 or index >= self.__size: raise Exception("Index out of bounds")
        
        current = self.__front
        for i in range(index): current = current.next
        return current.data

    '''
    Sets an element at a specicied index to a specified value and returns the value
    previously at the specified index. If the index parameter is outside the range of the
    list, this function raises an Exception.
    '''

    def set(self, index, value):
        if index < 0 or index >= self.__size: Exception

        current = self.__front
        for i in range(index): current = current.next

        toRet = current.data
        current.data = value
        return toRet

    '''
    If the index parameter is outside the range of the list, this function raises an
    Exception.
    '''

    def add(self, value, index=None):
        returnTrue = False
        
        if index is None:
            index = self.__size
            returnTrue = True
            
        self.__add(index, value, 0, self.__front)
        self.__size += 1
        if returnTrue: return True

    '''
    This function is part of a recursive pair with a private function.
    '''

    def __add(self, idx, value, currIdx, head):
        if idx == 0: self.__front = self.Node(value, self.__front)
        elif self.__front is None: raise Exception
        elif currIdx + 1 == idx: head.next = self.Node(value, head.next)
        else: self.__add(idx, value, currIdx + 1, head.next)

    '''
    Adds all elements of an iterable object to the list. Elements returned earlier by the
    iterable's call to next() will be added to earlier positions in the list. If the
    iterable parameter is not in fact iterable, this function raises an Exception.
    '''

    def addAll(self, iterable):
        try:
            for item in iterable: self.add(item)
        except TypeError as te: raise Exception

    '''
    If the index parameter is outside the range of the list, this function raises an
    Exception.
    '''

    def remove(self, index):
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

    '''
    Returns a string representation of the list, which is a comma-seperated list of values.
    This function is part of a recursive pair with a private function.
    '''

    def toString(self):
        if self.__front is None: return ""
        else: return self.__toString(self.__front)

    '''
    This function is part of a recursive pair with a public function.
    '''

    def __toString(self, head):
        if head.next is None: return str(head.data)
        else: return str(head.data) + ", " + self.__toString(head.next)

    '''
    Empties all elements from the list, resetting the size to 0.
    '''

    def clear(self):
        self.__front = None
        self.__size = 0

    '''
    Returns an iterator that allows this list to be used in for-in loops. It does so by
    creating an idea of a current index, which starts at 0.
    '''

    def __iter__(self):
        self.__current = self.__front
        return self

    '''
    Using fields crated by the iter() function, the function returns the next value in the
    list from the current index, and advances the current index by 1 element.
    '''

    def __next__(self):
        if self.__current is None: raise StopIteration
        ret = self.__current.data
        self.__current = self.__current.next
        return ret
    
    '''
    A Node is the smallest element of a linked list. It contains a peice of data and a reference to
    the next Node in the list.
    '''

    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    
    
if __name__ == '__main__':
    ll = linkedList()
    al = arrayList()
