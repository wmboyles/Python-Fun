from turtle import*

def vonKochRepl(s,depth):
    ht()
    pencolor("white")
    speed(0)
    if depth==0: return s
    out=""
    for c in s:
        if c=="f": out+="f+f-f-f+f"
        else: out+=c
    return vonKochRepl(out,depth-1)

def vonKoch(level):
    speed(0)
    pencolor("white")
    ht()
    a=vonKochRepl("f",level)
    for letter in a:
        if letter in "f": forward(10)
        elif letter=="-": right(90)
        elif letter=="+": left(90)

def prepare(L,trace=30):
    setundobuffer(None)
    bgcolor("black")
    setworldcoordinates(0,0,10*(3**L),10*(3**L))
    getscreen().tracer(trace)

def main(n=5):
    prepare(n)
    vonKoch(n)
    update()

main()
input()
