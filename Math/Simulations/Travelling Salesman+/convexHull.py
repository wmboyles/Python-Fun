from math import atan2

#Is the turn counter clockwise?
def CCW(p1, p2, p3):
    return (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0])


def jarvisMarch(gift):
    n = len(gift)  #Number of points in list
    pointOnHull = min(gift) #leftmost point in gift
    hull = [pointOnHull] #leftmost point guaranteed to be in hull
    
    while True:
        endpoint = gift[0]  #Candidate for next point in hull
        for j in range(1,n):
            if endpoint==pointOnHull or not CCW(gift[j],hull[-1],endpoint):
                endpoint = gift[j]
                
        pointOnHull = endpoint        
                
        #Check if we have completely wrapped gift
        if hull[0]==endpoint:
            break
        else:
            hull.append(pointOnHull)

    return hull


#Find the polar angle of a point relative to a reference point
def polarAngle(ref, point):
    return atan2(point[1]-ref[1],point[0]-ref[0])


def grahamScan(gift):
    gift = list(set(gift)) #Remove duplicates
    start = min(gift, key=lambda p: (p[1],p[0])) #Must be in hull
    gift.remove(start)

    S = sorted(gift,key=lambda point: polarAngle(start,point))
    hull = [start,S[0],S[1]]

    #Remove points from hull that make the hull concave
    for pt in S[2:]:
        while not CCW(hull[-2],hull[-1],pt):
            del hull[-1]
        hull.append(pt)

    return hull
