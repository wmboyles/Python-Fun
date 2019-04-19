from math import sqrt
from turtle import *

#Set to initial state of the planets
def setAll():
    global Planet1, Planet2, Planet3
    #Stationary Planet 1
    m1 = 1
    p1 = (-1,0)
    v1 = (-.3,-.5)
    a1 = (0,0)
    Planet1 = (m1,p1,v1,a1)

    #Orbiting Planet 1
    m2 = 1      #Mass
    p2 = (1,0)  #Position
    v2 = (.3,.6)  #Velocity
    a2 = (0,0)  #Acceleration
    Planet2 = (m2,p2,v2,a2)

#Magnitude of vector, v.
def magnitude(v):
    return sqrt(v[0]**2 + v[1]**2)

#Multiply a vector, v, by a scalar, s.
def scalarMult(s,v):
    return (s*v[0],s*v[1])

#Add and subtract vectors.
def vecAdd(v1,v2):
    return (v2[0]+v1[0],v2[1]+v1[1])

def vecSubtract(v1,v2):
    return (v2[0]-v1[0], v2[1]-v1[1])

#Get unit vector in same direction as vector, v.
def normalize(v):
    return scalarMult(1/magnitude(v),v)


#Calculate distance between planets
def calcDist(PlanetA, PlanetB):
    return magnitude(vecSubtract(PlanetA[1],PlanetB[1]))

#Calculate gravatational force between planets
def calcForce(PlanetA, PlanetB):
    #Acceleration force
    forceMag = (PlanetA[0]*PlanetB[0])/(calcDist(PlanetA, PlanetB))**2
    forceDir = normalize(vecSubtract(PlanetB[1],PlanetA[1]))
    forceVec = scalarMult(forceMag,forceDir)
    
    return forceVec

#Calculate acceleration of PlanetB due to gravity.
def calcAccel(PlanetA, PlanetB):
    return scalarMult(1/PlanetB[0],calcForce(PlanetA,PlanetB))

#Calculate velocity of PlanetB over time period, dt.
def calcVelocity(PlanetA, PlanetB, dt):
    return vecAdd(PlanetB[2], scalarMult(dt,calcAccel(PlanetA, PlanetB)))

#Calculate position of PlanetB over time period, dt.
def calcPos(PlanetA, PlanetB, dt):
    p= PlanetB[1]
    v = scalarMult(dt,vecAdd(scalarMult(.51,calcVelocity(PlanetA,PlanetB,dt)),scalarMult(.49,PlanetB[2])))
    a = scalarMult((dt**2)/2, vecAdd(scalarMult(.51, calcAccel(PlanetA,PlanetB)), scalarMult(.49, PlanetB[3])))
    
    return vecAdd(vecAdd(p, v),a)

#Update PlanetB's data with new calculated values.
def updatePlanet(PlanetA, PlanetB, dt):
    return (PlanetB[0],calcPos(PlanetA,PlanetB,dt),calcVelocity(PlanetA,PlanetB,dt),calcAccel(PlanetA,PlanetB))


#Simulates some number of steps with some stepsize and writes positions to text file
def simulate(steps=100, stepSize=.01, tracer=1000):
    setAll()
    global Planet1, Planet2, Planet3

    screen=Screen()
    screen.bgcolor("black")
    speed(0)
    setup(800,800)
    getscreen().tracer(tracer)
    setworldcoordinates(-5,-5,5,5)

    points=[]

    for i in range(steps):
        pu()
        ht()
        goto(Planet1[1])
        dot(3,"white")
        goto(Planet2[1])
        dot(2, "yellow")
        
        Planet2 = updatePlanet(Planet1, Planet2, stepSize)
        #Planet1 = updatePlanet(Planet2, Planet1, stepSize)

simulate(50000,.001,1000)
