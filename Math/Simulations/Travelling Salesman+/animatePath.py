import convexHull
import salesman
import paths
from turtle import*
from time import sleep


# Does all the setup, draws, points and lines
def animatePath(pts, bgColor="black", ptsColor="white", routeColor="white"):
    makeCanvas(extremes(pts), bgColor)
    plotPoints(pts, ptsColor)
        
    plotRoute(convexHull.grahamScan(pts), routeColor)
    plotRoute(salesman.bruteForce(pts), "green")
 
'''
Below functions are meant to be used in the above one
'''


# Finds the extreme x and y points
def extremes(points):
    minX = points[0][0]
    minY = points[0][1]
    maxX = points[0][0]
    maxY = points[0][1]
    for point in points[1:]:
        if point[0] < minX: minX = point[0]
        if point[0] > maxX: maxX = point[0]
        if point[1] < minY: minY = point[1]
        if point[1] > maxY: maxY = point[1]
    return (minX, minY, maxX, maxY)


# Makes a canvas o certain color from extremes
def makeCanvas(extr, color):
    screen = Screen()
    screen.colormode(255)
    minX, minY, maxX, maxY = extr
    diffX = .05 * (maxX - minX)
    diffY = .05 * (maxY - minY)
    screen.setworldcoordinates(minX - diffX, minY - diffY, maxX + diffX, maxY + diffY)
    screen.bgcolor(color)


# Plots the points of gven color in order given
def plotPoints(points, col):
    color(col)
    speed(0)
    ht()
    penup()
    for point in points:
        setpos(point)
        dot()


# Draws lines in given color in given order
def plotRoute(route, col, closed=True):
    if closed and route[-1] != route[0]:
        route += [route[0]]
    color(col)
    penup()
    goto(route[0])
    pendown()
    for point in route[1:]: goto(point)
    hideturtle()


def main(size):
    clear()
    animatePath(paths.sorted(size))
    onkey(main, "Up")
    listen()


if __name__ == '__main__':
    while True:
        main(7)
        sleep(1)
