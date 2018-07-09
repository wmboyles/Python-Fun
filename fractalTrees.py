from turtle import*
from math import pi, degrees

screen=Screen()


#Creates the black background & positions turtle
def create(cords=(1000,1000),window=(500,500)):
    screen.colormode(255)
    setup(window[0],window[1])
    screen.setworldcoordinates(-100,-100,cords[0],cords[1])
    screen.bgcolor("black")
    screen.tracer(240)

    #turtle
    setundobuffer(None)
    speed(0)
    ht()
    color("white")
    pu()
    goto((cords[0]/2,0))
    dot()
    seth(90)
    pd()


#Recursively draws branches, rightmost first
def branch(length,angle,minLength=16):
    fd(length)
    x,y,a=xcor(),ycor(),heading()
    
    rt(angle)
    if length>=minLength: branch(2*length/3,angle,minLength)

    pu()
    goto((x,y))
    seth(a)
    pd()
    
    lt(angle)
    if length>=minLength: branch(2*length/3,angle,minLength)

#Example
create((1000,1500),(700,700))
branch(512,30,2)
