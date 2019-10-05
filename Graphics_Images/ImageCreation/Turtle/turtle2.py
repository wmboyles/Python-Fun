from turtle import*
from math import sin, cos, pi, e
from random import randint

a = Turtle()
screen = Screen()
screen.colormode(255)

RGV = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple"]
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']


def regPolygon(t, sides, sl, fill):
    if fill == True: t.begin_fill()
    for i in range(int(sides)):
        if fill == True: t.color(colors[i % 7])
        t.fd(sl)
        t.lt(180 - (sides - 2) * 180 / sides)
    t.end_fill()

    
def star(t, points, sl, fill):
    if fill == True: t.begin_fill()
    if points == 3 or points == 4: regPolygon(t, points, sl, fill)
    else:
        for i in range(points):
            if fill == True: t.color(colors[i % 7])
            t.fd(sl)
            t.lt(360 / points)  # 3->60, 4->90, 5->72, 6->60, 8->45
            t.fd(sl)
            t.rt(720 / points)
    t.end_fill()

def pentagram(t, points, sl, fill):
    if fill: t.begin_fill()
    if points == 3 or points == 4: regPolygon(t, points, sl, fill)
    else:
        for i in range(points):
            t.fd(sl)
            t.rt((360 - 360/(points))/2)
    t.end_fill()


def draw_art():
    window = Screen()
    window.bgcolor("black")
    # Turtle Brad
    brad = Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(0)
    brad.pensize(2)
    for i in range(1, 37):
        regPolygon(brad, 4, 200, False)
        brad.right(10)
    # Turtle Angie
    angie = Turtle()
    angie.shape("turtle")
    angie.color("blue")
    angie.speed(0)
    angie.pensize(2)
    size = 1
    for _ in range(300):
        angie.forward(size)
        angie.right(91)
        size = size + 1
    angie.hideturtle()
    window.exitonclick()


def myArt1(a):
    screen.bgcolor("black")
    a.color("Red")
    for i in range(0, 37):
        # regPolygon(a,sides,sl,False)
        a.circle(100)
        a.rt(10)
        regPolygon(a, 1, 10, False)
    a.hideturtle()


def myArt2(a):
    screen.bgcolor("black")
    a.pensize(1.6)
    a.color("aqua")
    for i in range(0, 245):
        a.fd(5 + 2 * i)
        a.rt(89)
    a.hideturtle()


def myArt3(a):
    screen.bgcolor("black")
    for i in range(1000):
        a.color((255 - int(i * 255 / 361)) % 256, int(i * 256 / 361) % 256, (255 - int(255 * i / 360)) % 256)
        a.width(i / 360 + 1)
        a.fd(i)
        a.lt(89)
    a.hideturtle()

    
a.speed(0)
for i in range(3,10):
    a.color(colors[i%6])
    pentagram(a,i,300,False)

