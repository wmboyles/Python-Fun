from math import atan2

"""
Chan's algorithm idea
*   While m < h ... (square m at each iteration)

*   Compute K <= 1 + n/m smaller sub-hulls of size at most p each using a Graham Scan.
    This takes O(p log p) time.

*   Do a Jarvis March over the points in the sub hulls.
    This takes O(K log m) time.

*   So, the entire algorithm runs in O(n log h) time. For h << n,
    which is likely to happen as n gets large, this is very efficient.
"""


# Is the turn counter clockwise?
def CCW(p1, p2, p3):
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0])


def jarvisMarch(gift): # O(n*h), where h is the number of points in the hull
    n = len(gift)  # Number of points in list
    pointOnHull = min(gift)  # leftmost point in gift
    hull = [pointOnHull]  # leftmost point guaranteed to be in hull
    
    while True:
        endpoint = gift[0]  # Candidate for next point in hull
        for j in range(1, n):
            if endpoint == pointOnHull or not CCW(gift[j], hull[-1], endpoint):
                endpoint = gift[j]
                
        pointOnHull = endpoint        
                
        # Check if we have completely wrapped gift
        if hull[0] == endpoint:
            break
        else:
            hull.append(pointOnHull)

    return hull


# Find the polar angle of a point relative to a reference point
def polarAngle(ref, point):
    return atan2(point[1] - ref[1], point[0] - ref[0])


def grahamScan(gift): #O(n log n) algorithm
    gift = list(set(gift))  # Remove duplicates O(n)
    start = min(gift, key=lambda p: (p[1], p[0]))  # extreme point must be in hull O(n)
    gift.remove(start)

    S = sorted(gift, key=lambda point: polarAngle(start, point)) #O(n log n)
    hull = [start, S[0], S[1]]

    # Remove points from hull that make the hull concave
    for pt in S[2:]:    # O(n) -- each point is considered at most twice
                        # It's either deleted in the while, or appended in the for
        while not CCW(hull[-2], hull[-1], pt):
            del hull[-1] #Assumes this is O(1) like in a stack
        hull.append(pt)

    return hull
