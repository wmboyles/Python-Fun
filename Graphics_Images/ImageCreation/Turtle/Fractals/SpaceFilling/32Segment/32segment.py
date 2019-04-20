from turtle import*


def getCurve(n, curve='F+F+F+F'):
    if n == 0: return curve
    out = ""
    for e in curve:
        if e == 'F': out += '-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+'
        else: out += e
    return getCurve(n - 1, out)


def drawCurve(curve):
    for e in curve:
        if e == 'F': fd(1)
        elif e == '+': lt(90)
        else: rt(90)


def main(n=2, trace=100):
    bgcolor("black")
    setworldcoordinates(-35, -35, 100, 100)
    tracer(trace)

    color("white")
    ht()
    speed(0)
    setundobuffer(None)
    drawCurve(getCurve(n))
    update()


main()
input()
