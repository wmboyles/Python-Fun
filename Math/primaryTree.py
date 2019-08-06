from turtle import*

'''
A primaryTree is a way of ordering the natural numbers into a binary tree in a way
so that numbers are arranged by their primeness. A number
'''
class primaryTree:
    def __init__(self):
        self.__root = None
        self.__size = 0
        self.__primes = []
        self.__turtleSetup()


    def __turtleSetup(self):
        self.__t = Turtle()
        self.__t.speed(0)
        self.__t.pu()
        self.__t.color("white")
        self.__t.goto((0,100))
        self.__t.setheading(270) #face down
        self.__t.st()

    def add(self):
        #turtle setup stuff
        self.__t.pu()
        self.__t.goto((0,100))
        self.__t.setheading(270)
        self.__t.pd()
        turnAngle = 85 #how far the heading of the turtle will change from vertically down
        turnDelta = 5 #how much less should the heading of turtle change from turnAngle
        initDist = 100 #the length of the first branch in the tree
        distMult = 1.1 #the ratio of the lengths of the previous branch to the current branch
        
        self.__size+=1
        currentNode = self.__root
        if self.__root is None: #special case of creating the root (just 1)
            self.__root = self.Node(self.__size)

            self.__t.write(self.__size) #create a dot at a node and write number
            self.__t.dot()
            
            return
        elif len(self.__primes)==0: #special case of adding the prime on left (just 2)
            currentNode.left = self.Node(self.__size)

            self.__t.rt(turnAngle) #from turtle's perspective, left branch is right turn
            self.__t.forward(initDist) #64 is branch length for first layer
            self.__t.setheading(270)
            self.__t.write(self.__size) #create a dot at a node and write number
            self.__t.dot()
            
            self.__primes.append(self.__size)
            return
            
        possiblePrime = True
        depthCount=0
        for prime in self.__primes: #General case of adding all other numbers
            if self.__size%prime == 0:
                possiblePrime = False
                if currentNode.left is None:
                    currentNode.left = self.Node(self.__size)

                    self.__t.rt(turnAngle-(turnDelta*depthCount)) #from turtle's perspective, left branch is right turn
                    self.__t.forward(initDist/(distMult**depthCount)) #64 is branch length for first layer
                    self.__t.setheading(270)
                    self.__t.write(self.__size) #create a dot at a node and write number
                    self.__t.dot()
                    
                    break
                else:
                    currentNode = currentNode.left

                    self.__t.rt(turnAngle-(turnDelta*depthCount)) #from turtle's perspective, left branch is right turn
                    self.__t.forward(initDist/(distMult**depthCount)) #64 is branch length for first layer
                    self.__t.setheading(270)
                    depthCount+=1
                    
            else:
                if currentNode.right is None:
                    currentNode.right = self.Node(self.__size)

                    self.__t.lt(turnAngle-(turnDelta*depthCount)) #from turtle's perspective, right branch is left turn
                    self.__t.forward(initDist/(distMult**depthCount)) #64 is branch length for first layer
                    self.__t.setheading(270)
                    self.__t.write(self.__size) #create a dot at a node and write number
                    self.__t.dot()
                    
                    break
                else:
                    currentNode =currentNode.right

                    self.__t.lt(turnAngle-(turnDelta*depthCount)) #from turtle's perspective, right branch is left turn
                    self.__t.forward(initDist/(distMult**depthCount)) #64 is branch length for first layer
                    self.__t.setheading(270)
                    depthCount+=1

        if possiblePrime: self.__primes.append(self.__size)
        self.__t.ht()

    #Returns the maximum height (depth) of the tree. This will usually be the same as len(primes).
    def maxHeight(self): return self.__root.maxHeight() if self.__root is not None else 1

    #Returns a list of all prime numbers currently in the tree
    def primes(self): return self.__primes

    #Returns a string representation of the tree as the in-order traversal.
    def __str__(self): return self.__root.__str__()

    #Returns the number of Nodes in the tree.
    def __len__(self): return self.__size

    #A Node is a single element in the tree. It contains a value and possibly left and right subnodes.
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        #Returns the in-order traveral of the subtree with this node as the root
        def __str__(self):
            string = "" if self.left is None else self.left.__str__()
            string += str(self.value) if len(string)==0 else " "+str(self.value)
            string += "" if self.right is None else " "+self.right.__str__()
            return string
        
        #Finds the maximum height of the tree with this Node as the root Node
        def maxHeight(self):
            leftHeight = 0 if self.left is None else self.left.maxHeight()
            rightHeight = 0 if self.right is None else self.right.maxHeight()
            return 1+max(leftHeight,rightHeight)


# Makes a canvas of a certain color from extreme points
def makeCanvas(extr=((-150,-500,400,100)), bgColor="black"):
    screen = Screen()
    screen.colormode(255)
    minX, minY, maxX, maxY = extr
    diffX = .05 * (maxX - minX)
    diffY = .05 * (maxY - minY)
    screen.setworldcoordinates(minX - diffX, minY - diffY, maxX + diffX, maxY + diffY)
    screen.bgcolor(bgColor)
    
makeCanvas()
p = primaryTree()
for i in range(100): p.add()

