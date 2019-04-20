from turtle import*


def getCurve(n, curve='F'):
    if n == 0: return curve
    out = ""
    for e in curve:
        if e == 'F': out += 'F[+F]F[-F]F'
        else: out += e
    return getCurve(n - 1, out)


def drawCurve(curve):
    posts = []
    for e in curve:
        if e == 'F': fd(1)
        elif e == '+': rt(25)
        elif e == '-': lt(25)
        elif e == '[': posts.append((pos(), heading()))
        elif e == ']':
            pu()
            goto(posts[-1][0])
            setheading(posts[-1][1])
            pd()
            del posts[-1]


def main(n=4, trace=250):
    bgcolor("black")
    setworldcoordinates(-40, 0, 40, 80)
    tracer(trace)

    color("green")
    ht()
    lt(90)
    speed(0)
    setundobuffer(None)
    drawCurve(getCurve(n))
    update()


main()
input()
