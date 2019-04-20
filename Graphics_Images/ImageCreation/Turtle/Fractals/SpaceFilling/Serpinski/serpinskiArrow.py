from turtle import*
from math import sqrt


def getCurve(n, curve='A'):
    if n == 0: return curve
    out = ""
    for e in curve:
        if e == 'A':
            out += 'B-A-B'
        elif e == 'B':
            out += 'A+B+A'
        else:
            out += e
    return getCurve(n - 1, out)


def drawCurve(curve):
    for e in curve:
        if e in 'AB': fd(1)
        elif e == '+': lt(60)
        else: rt(60)


def main(n=10, trace=30):
    bgcolor("black")
    tracer(trace)
    if n % 2: setworldcoordinates(0, -(2 ** n) * sqrt(3) / 2, 2 ** n, 0)
    else: setworldcoordinates(0, 0, 2 ** n, (2 ** n) * sqrt(3) / 2)

    speed(0)
    setundobuffer(None)
    pencolor("white")
    ht()
    drawCurve(getCurve(n))
    update()


main(8, 1000)
input()
