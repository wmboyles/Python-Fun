from turtle import*


def getCurve(n, curve='L'):
    if n == 0: return curve
    out = ""
    for e in curve:
        if e == 'L': out += '+RF-LFL-FR+'
        elif e == 'R': out += '-LF+RFR+FL-'
        else: out += e
    return getCurve(n - 1, out)


def drawCurve(curve):
    for e in curve:
        if e == 'F': fd(1)
        elif e == '+': rt(90)
        elif e == '-': lt(90)


def main(n=5, trace=0):
    bgcolor("black")
    setworldcoordinates(0, -(2 ** n), (2 ** n), 0)
    tracer(trace)
    color("white")
    ht()
    speed(0)
    setundobuffer(None)
    drawCurve(getCurve(n))
    update()


main()
input()
