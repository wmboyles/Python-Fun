from math import sqrt, factorial
from itertools import permutations
from random import randint, shuffle


def NN(pts):
    NNRoute = [pts[0]]
    unvisitedPts = pts[1:]

    for i in range(0,len(unvisitedPts)):
        nextPt = NNnextPt(NNRoute[-1],unvisitedPts)
        unvisitedPts.remove(nextPt)
        NNRoute.append(nextPt)

    NNRoute.append(NNRoute[0])
    return NNRoute


def NNnextPt(start,unvisited):
    minPoint = unvisited[0]
    minDist=dist(start,minPoint)
    for point in unvisited:
        d=dist(start,point)
        if d<minDist:
            minDist=d
            minPoint=point
    return minPoint


def dist(p1,p2):
    (x1,y1),(x2,y2)=p1,p2
    return sqrt((y2-y1)**2 + (x2-x1)**2)


def bruteForce(pts):
    start = pts[0]
    allRoutes = list(permutations(pts[1:])) #Currently list of unclosed paths

    #Make into list of lists of closed routes
    for i in range(0,len(allRoutes)): 
        allRoutes[i] = list(allRoutes[i])
        allRoutes[i].insert(0,pts[0])
        allRoutes[i].append(pts[0])

    bestRoute = allRoutes[0]
    bestRouteLen = routeLength(bestRoute)

    for i in range(1,len(allRoutes)):
        newRoute = allRoutes[i]
        newRouteLen = routeLength(newRoute)
        if newRouteLen<bestRouteLen:
            bestRouteLen = newRouteLen
            bestRoute = newRoute

    return bestRoute
        

def routeLength(route):
    routeLen=0
    for i in range(1,len(route)): routeLen+=dist(route[i-1],route[i])
    return routeLen


def NNSwap(pts,swaps): #2opt swap starting from NN route -- suboptimal
    bestRoute = NN(pts)
    bestPath = bestRoute[1:]
    bestRouteLength = routeLength(bestRoute)
    
    for i in range(swaps):
        swap1 = randint(0,len(pts)-1)
        swap2 = randint(0,len(pts)-1)
        
        newPath = swap(bestPath,swap1,swap2)#currently open path
        
        newRoute = newPath
        newRoute.append(newRoute[0])
        newRouteLength = routeLength(newRoute)
        
        if newRouteLength<bestRouteLength:
            bestRoute = newRoute
            bestPath = bestRoute[1:]
            bestRouteLength = newRouteLength

    return bestRoute


def swap(path,i1,i2):
    pathCopy = path[0:]
    temp = pathCopy[i1]
    pathCopy[i1] = pathCopy[i2]
    pathCopy[i2] = temp
    return pathCopy


def randomPath(pts):
    copy = pts[0:]
    shuffle(copy)
    copy.append(copy[0])
    return copy


def randPaths(pts,trials):
    copy=pts[0:]
    bestPath = randomPath(copy)
    bestPathLen = pathLength(bestPath)
    for i in range(1,trials):
        randPath = randomPath(copy)
        randLen = pathLength(randPath)
        if randLen<bestPathLen:
            bestPathLen=randLen
            bestPath=randPath
            
    return bestPath
