from turtle import*
from math import pi, degrees, sqrt


# Recursively draws branches, rightmost first
def branch(length, angle=90, minLength=8):
    fd(length)
    x, y, a = xcor(), ycor(), heading()
    
    rt(angle)
    if length >= minLength: branch(length / sqrt(2), angle, minLength)

    pu()
    goto((x, y))
    seth(a)
    pd()
    
    lt(angle)
    if length >= minLength: branch(length / sqrt(2), angle, minLength)


def main(l=512, a=90, m=8, trace=240):
    setup(700, 700)
    setworldcoordinates(-200, 0, 1225, 1025)
    bgcolor("black")
    tracer(trace)

    setundobuffer(None)
    color("white")
    speed(0)
    ht()

    pu()
    goto((510, 0))
    seth(a)
    pd()
    
    branch(l, a, m)
    update()


main()
input()
