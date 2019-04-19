from turtle import*

def middleCompliment(curve):
    l=len(curve)
    letter = str((int(curve[l//2])-1)%2)
    l1 = curve[0:l//2]
    l2 = curve[l//2+1:]
    return l1+letter+l2

def nextCurve(curve,steps):
    if steps!=0:
        return nextCurve(curve+'1'+middleCompliment(curve),steps-1)
    else: return curve

def dragon_setup():
    screen=Screen()
    setup(700,700)
    screen.setworldcoordinates(-200,0,500,700)
    screen.bgcolor("black")
    screen.tracer(240)

    setundobuffer(None)
    ht()
    speed(0)
    color("white")
    pu()
    goto((250,250))
    seth(0)
    pd()

def dragon(curve):
    for char in curve:
        fd(10)
        if int(char)==1: lt(90)
        else: rt(90)

def main(n=10):
    curve = nextCurve("1",n)
    dragon_setup()
    dragon(curve)
    update()

main()    
input()
