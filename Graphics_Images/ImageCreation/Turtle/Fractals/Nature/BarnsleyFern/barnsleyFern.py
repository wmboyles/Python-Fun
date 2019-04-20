from random import random
from turtle import*


def nextPt(currentPt):
    rand = random()
    nextX, nextY = currentPt
    
    if rand < .01:
        nextX = 0
        nextY = .16 * currentPt[1]
    elif rand < .86:
        nextX = .85 * currentPt[0] + .04 * currentPt[1]
        nextY = -.04 * currentPt[0] + .85 * currentPt[1] + 1.6
    elif rand < .93:
        nextX = .2 * currentPt[0] - .26 * currentPt[1]
        nextY = .23 * currentPt[0] + .22 * currentPt[1] + 1.6
    else:
        nextX = -.15 * currentPt[0] + .28 * currentPt[1]
        nextY = .26 * currentPt[0] + .24 * currentPt[1] + .44

    return (nextX, nextY)


def drawPt(pt):
    speed(0)
    ht()
    pu()
    goto(pt)
    dot(2, "green")


def drawFern(tracer=1000):
    bgcolor("black")
    pencolor("white")
    setundobuffer(None)
    setup(700, 700)
    getscreen().tracer(tracer)
    setworldcoordinates(-2.182, 0, 2.6558, 9.9983)

    X, Y = 0, 0
    drawPt((X, Y))
    for i in range(10 ** 6):
        X, Y = nextPt((X, Y))
        drawPt((X, Y))


drawFern()
    
