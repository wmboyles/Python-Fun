from turtle import*

def serpRepl(s,level):
    if level==0: return s
    out=""
    for c in s:
        if c=="f": out+="f-g+f+g-f"
        elif c=="g": out+="gg"
        else: out+=c
    return serpRepl(out,level-1)

def serpinski(level):
    a=serpRepl("f-g-g",level)
    for letter in a:
        if letter in "fg": forward(10)
        elif letter=="-": right(120)
        elif letter=="+": left(120)

def main(L=7,trace=30):
    F=10*(2**L)
    setup(700,700)
    bgcolor("black")
    getscreen().tracer(trace)
    setworldcoordinates(0,-F,F,0)
    
    setundobuffer(None)
    color("white")
    ht()
    
    serpinski(L)
    update()

main()
input()
