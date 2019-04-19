from turtle import*

def getCurve(n,curve='A'):
    if n==0: return curve
    out=""
    for e in curve:
        if e=='A': out+='A-B--B+A++AA+B-'
        elif e=='B': out+='+A-BB--B-A++A+B'
        else: out+=e
    return getCurve(n-1,out)

def drawCurve(curve):
    for e in curve:
        if e in 'AB': fd(1)
        elif e=='+': lt(60)
        elif e=='-': rt(60)

def main(n=4,trace=100):
    bgcolor("black")
    setworldcoordinates(-37,-55,20,2)
    tracer(trace)

    color("white")
    ht()
    speed(0)
    setundobuffer(None)
    drawCurve(getCurve(n))
    update()

main()
input()
