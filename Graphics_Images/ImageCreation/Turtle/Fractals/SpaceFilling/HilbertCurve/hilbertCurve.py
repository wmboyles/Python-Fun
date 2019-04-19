from turtle import*
from math import cos, radians

def hilbertCurve(L, ang, size=1, trace=30):
    colormode(0)
    bgcolor("black")
    setundobuffer(None)
    getscreen().tracer(trace)
    X=size*((2*cos(radians(ang))+2)**L -1) +1
    setworldcoordinates(-X,0,0,X)
    goto((-X,X))
    ht()
    draw(L,ang,size)

def draw(level, ang, size=1):
    pencolor("white")
    speed(0)
    if level==0: return

    rt(ang)
    draw(level-1,-ang,size)
    fd(size)
    lt(ang)
    draw(level-1,ang,size)
    fd(size)
    draw(level-1,ang,size)
    lt(ang)
    fd(size)
    draw(level-1,-ang,size)
    rt(ang)

def main(n=5,ang=90):
    setup(700,700)
    hilbertCurve(n,ang)
    update()

main()
input()
