from turtle import*
from math import sqrt

def getCurve(n,curve='F'):
    if n==0: return curve
    out=""
    for e in curve:
        if e=='F': out+="F+F--F+F"
        else: out+=e
    return getCurve(n-1,out)

def drawCurve(curve):
    for e in curve:
        if e=='F': fd(1)
        elif e=='+': lt(60)
        else: rt(60)

def main(n=5,trace=30):
    bgcolor("black")
    m=sqrt(3)/2
    setworldcoordinates(0,-m*3**n,3**n,m*3**(n-1))
    tracer(trace)

    color("white")
    ht()
    speed(0)
    setundobuffer(None)
    for i in range(3):
        drawCurve(getCurve(n))
        rt(120)
    update()

main()
input()
