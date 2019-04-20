from turtle import*


def compliment(s):
    out = ""
    for c in s:
        if c == '0': out += '1'
        else: out += '0'
    return out


def getSnowflake(n):
    snowflake = '0'
    for i in range(n):
        snowflake += compliment(snowflake)

    return snowflake


def prepare():
    setup(700, 700)
    L = 3 ** 6
    setworldcoordinates(-L, -L / 2, 0, L / 2)
    bgcolor("black")


def main():
    prepare()
    ht()
    speed(0)
    pencolor("white")
    width(0)
    setundobuffer(None)
    getscreen().tracer(100)
    path = getSnowflake(15)
    for i in range(3):
        for e in path:
            if e == '0': fd(1)
            else: lt(60)
        
    update()


main()
input()
