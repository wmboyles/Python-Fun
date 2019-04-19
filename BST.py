class binaryTree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def size(self): return self.__size

    def add(self, value):
        self.__root = self.__add(self.__root, value)
        self.__size += 1

    def __add(self, stem, value):
        if stem is None: stem = self.Node(value)
        elif stem.data > value: stem.left = self.__add(stem.left, value)
        elif stem.data < value: stem.right = self.__add(stem.right, value)
        else: raise Exception #duplicate

        return stem

    def remove(self, value):
        self.__root = self.__remove(self.__root, value)
        self.__size -= 1

    def __remove(self, stem, value):
        if stem is None: return stem
        elif value < stem.data: stem.left = self.__remove(stem.left, value)
        elif value > stem.data: stem.right = self.__remove(stem.right, value)
        else:
            if stem.left is None:
                temp = stem.right
                stem = None
                return temp
            elif stem.right is None:
                temp = stem.left
                stem = None
                return temp
            else:
                temp = self.__minValueNode(stem.right)
                stem.data = temp.data
                stem.right = self.__remove(stem.right, temp.data)

        return stem

    def __minValueNode(self, stem):
        if stem.left is None: return stem
        else: return self.__minValueNode(stem.left)

    def contains(self, value): return self.__contains2(self.__root, value)

    def __contains2(self, stem, value):
        if stem is None: return False
        elif stem.data == value: return True
        elif stem.data < value: return self.__contains2(stem.right, value)
        elif stem.data > value: return self.__contains2(stem.left, value)
        else: raise Exception #You shouldn't be able to get here

    def toString(self): return self.__toString(self.__root)[2:-2] #In-order

    def __toString(self, stem):
        if stem is None: return ", "
        else: return self.__toString(stem.left) + str(stem.data) + self.__toString2(stem.right)

    class Node:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = left
            self.right = right



bt = binaryTree()
        
