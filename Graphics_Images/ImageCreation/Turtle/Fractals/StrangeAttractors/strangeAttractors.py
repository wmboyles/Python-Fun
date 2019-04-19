from turtle import*
from random import randint
from math import sin,cos,pi

points=[]
N=0

#give equally speced points around a circle
def circle(n):
    path=[]
    speed(0)
    for i in range(n):
        path.append((340*cos(2*pi*(i/n))+350,340*sin(2*pi*(i/n))+350))
    return path


#find the ceter of mass of the points
def centerMass(pts):
    speed(0)
    l=len(pts)
    xSum,ySum=0,0
    for point in pts:
        xSum+=point[0]
        ySum+=point[1]
    return (xSum/l,ySum/l)


#Create the anvas to contain all relevant points
def prepare():
    setup(700,700)
    speed(0)
    bgcolor("black")
    setworldcoordinates(0,0,700,700)

    #plot points
    for point in points:
        pu()
        goto(point)
        dot(2,"white")

    pu()
    goto(centerMass(points))
    dot()


#Find the weighted average of p1 and p2
def Npoint(p1,p2,n=2):
    return (( ((n-1)*p1[0])+p2[0] )/n,( ( (n-1)*p1[1])+p2[1])/n)


#Actually draw some fractals
def drawMain():
    ht()
    setundobuffer(None)
    speed(0)
    
    for i in range(10000):
        selection = randint(0,len(points)-1)
        goto(Npoint(points[selection],pos(),(N+1)/2))
        dot(2,"white")

def main():
    global points, N
    N =int(input("N: "))
    getscreen().tracer(500)
    points = circle(N)
    prepare()
    drawMain()

main()
