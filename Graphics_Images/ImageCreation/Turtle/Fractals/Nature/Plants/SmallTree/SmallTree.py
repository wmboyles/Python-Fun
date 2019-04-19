from turtle import*

def getCurve(n,curve='X'):
    if n==0: return curve
    out=""
    for e in curve:
        if e=='X': out+='F[+X][-X]FX'
        elif e=='F': out+='FF'
        else: out+=e
    return getCurve(n-1,out)

def drawCurve(curve):
    posts=[]
    for e in curve:
        if e=='F': fd(1)
        elif e=='+': rt(25)
        elif e=='-': lt(25)
        elif e=='[': posts.append((pos(),heading()))
        elif e==']':
            pu()
            goto(posts[-1][0])
            setheading(posts[-1][1])
            pd()
            del posts[-1]

def main(n=7,trace=250):
    bgcolor("black")
    setworldcoordinates(-70,0,70,260)
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
