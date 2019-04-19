from math import sin,cos,pi
from random import randint
from salesman import NN

#Draws a circle of n points
def circle(n):
    path=[]
    for i in range(n):
        path.append((n*cos(2*pi*(i/n)),n*sin(2*pi*(i/n))))
    return path

#Returns n random points
def random(n):
    randPath=[((randint(-n,n),randint(-n,n))) for i in range(n)]
    return randPath

#returns a path with the points in Nearest-Neighbor order
#This way is faster for plotting than random ordered points
def sorted(n): return NN(random(n))

#Gives a path such that every point is directly connected to every other
def complete(pts):
    allPath=[]
    for j in range(len(pts)):
        point = pts[j]
        i=pts.index(point)
        L=pts[j:i]+pts[i+1:]
        L=interweave(L,point)
        allPath+=L
    return allPath

#Interweaves (like perfect card shuffle) two lists
def interweave(l,t):
    for i in range(0,2*len(l)-1,2):
        l.insert(i,t)
    return l

#gives path connecting every point to the center of mass point
def radialCM(pts):
    CM = centerMass(pts)
    return interweave(pts,CM)

#Gives point that is center of mass of given points
def centerMass(pts):
    l=len(pts)
    xSum,ySum=0,0
    for point in pts:
        xSum+=point[0]
        ySum+=point[1]
    return (xSum/l,ySum/l)
    
