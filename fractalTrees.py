from turtle import*
from math import pi, degrees

screen=Screen()


#Creates the black background & positions turtle
def setup(cords):
    screen.colormode(1)
    screen.setworldcoordinates(0,0,cords[0],cords[1])
    screen.bgcolor("black")

    #turtle
    speed(0)
    ht()
    color("white")
    pu()
    goto((coords[0]/2,0))
    towards((cords[0]/2,cords[1]))
    pd()


#Recursively draws branches, rightmost first
def branch(length,angle,maxLength=16):
    forward(length)
    x,y,a=xcor(),ycor(),heading()
    
    rt(angle)
    if length>=maxL: branch(2*length/3,angle,maxLength)

    pu()
    goto((x,y))
    seth(a)
    pd()
    
    lt(angle)
    if length>=maxL: branch(2*length/3,angle,maxLength)


setup((1000,1000)) #Keep these two numbers the same to avoid distortions.
branch(512,degrees(pi/2),2)
