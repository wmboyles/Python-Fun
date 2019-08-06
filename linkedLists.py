class linkedList:
    #Creates a new, empty linked list
    def __init__(self):
        self.__size = 0
        self.__front = None

    #Returns the number of elements in the list
    def size(self):
        return self.__size

    #Returns the value at a specific index
    def get(self, idx):
        if(idx < 0 or idx >= self.__size):
            raise Exception("Index out of bounds") #Better exception to throw?

        current = self.__front
        for i in range(0, idx):
            current = current.next

        return current.value

    #Sets the value at a given index and returns the previous value
    def set(self, idx, val):
        if(idx < 0 or idx >= self.__size):
            raise Exception("Index out of bounds") #Better Exception to throw?

        current = self.__front
        value = None #Value to return
        for i in range(0, idx):
            current = current.next

        value = current.value
        current.value = val
        return value

    #Adds a given value at a given index in the list. Defaults to appending
    def add(self, val, idx = None):
        if idx is None:
            idx = self.__size
        
        if(idx < 0 or idx > self.__size):
            raise Exception("Index out of bounds") #Better exception to throw?

        if idx == 0: #Special Case: Adding to front of list
            self.__front = self.__Node(val, self.__front)
        else: #General Case: Adding to middle and end of list
            current = self.__front
            for i in range(1, idx): #Traverse to Node before insertion point
                current = current.next

            current.next = self.__Node(val, current.next)

        self.__size+=1

    #Removes a Node from the list and returns the removed value 
    def remove(self, idx):
        if(idx < 0 or idx > self.__size - 1):
            raise Exception("Index out of bounds") #Better eception to throw?

        value = None #Value of removed node
        if idx == 0: #Special Case: Removing from front of list
            value = self.__front.value
            self.__front =self.__front.next
        else: #General Case: Removing from middle or end of list
            current = self.__front
            for i in range(1, idx): #Traverse to Node before removal point
                current = current.next

            value = current.next.value
            current.next = current.next.next

        self.__size-=1
        return value

    #Returns the index of a given value in the list, else -1
    def indexOf(self, val):
        current = self.__front
        for i in range(0, self.__size):
            if(current.value == val):
                return i
            current = current.next

        return -1

    class __Node:
        value = None
        next = None
        
        #Creates a new Node given a value and next Node reference
        def __init__(self, value, next):
            self.value = value
            self.next = next

class RLL:
    def __init__(self):
        self.__front = None

    def size(self):
        if self.__front is None:
            return 0
        else:
            return self.__front.size()

    def get(self, idx):
        return self.__front.get(idx)

    def set(self, idx, val):
        return self.__front.set(idx, val)

    def add(self, val, idx = None):
        if self.__front is None:
            self.__front = self.__Node(val, self.__front)
        else:
            self.__front.add(val, idx)

    def remove(self, idx):
        if idx==0:
            value = self.__front.value
            self.__front = self.__front.next
            return value
        else:
            return self.__front.remove(idx)

    def indexOf(self, val):
        idx = self.__front.indexOf(val)
        if idx is None:
            return -1
        else:
            return idx

    class __Node:
        def __init__(self, value, next=None):
            self.value = value #Don't need private variables b/c class is private
            self.next = next

        def size(self):
            if self.next is None:
                return 1
            else:
                return 1 + self.next.size()

        def get(self, idx):
            if idx == 0:
                return self.value
            else:
                return self.next.get(idx - 1)
        
        def set(self, idx, val):
            if idx == 0:
                value = self.value
                self.value = val
                return value
            else:
                return self.next.set(idx - 1, val)
        
        def add(self, val, idx):
            if idx is None: #No given index means appending at end
                if self.next is None: #At end of list
                    self.next = self.__class__(val, self.next) #Creates new class instance
                else: #Not yet at end of list
                    self.next.add(val, None)
            elif idx == 1: #At correct index for insertion
                self.next = self.__class__(val, self.next)
            else: #Not yet at correct index
                self.next.add(val, idx - 1)
        
        def remove(self, idx):
            if idx == 1:
                value = self.next.value
                self.next = self.next.next
                return value
            else:
                return self.next.remove(idx-1)

        def indexOf(self, val):
            if self.value == val:
                return 0
            elif self.next is None:
                return -1
            else:
                idx = self.next.indexOf(val)
                if idx == -1: #Lets the -1 (not in list) propogate back
                    return -1
                else:
                    return 1 + idx
    
                
        
        
