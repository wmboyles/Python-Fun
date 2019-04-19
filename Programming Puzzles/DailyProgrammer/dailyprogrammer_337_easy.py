
#Part One

from math import pi


WIRELENGTH=100
radius=WIRELENGTH/2
SectorLen = WIRELENGTH-2*radius #=radius*angle
Angle = SectorLen/radius
AreaCompare = (Angle/2)*(radius**2)
Area = AreaCompare

while(abs(Area)>=abs(AreaCompare)):
    radius-=.0001
    AreaCompare = Area
    SectorLen = WIRELENGTH-2*radius #=radius*angle
    Angle = SectorLen/radius
    Area = (Angle/2)*(radius**2)
    
print(Angle*(180/pi)) #Convert to degrees


#Part 2

from math import sqrt

A = [0,20]  #(x,y) coordinates of villages A,B and of pipe
B = [100,30]
P = [A[0]+.001,0]

dist = sqrt((P[0])**2 + (20+P[1])**2) + sqrt((100-P[0])**2 + (30)**2)
distCompare = dist

while(dist<=distCompare):
    P[0]+=.0001
    distCompare = dist
    dist = sqrt((P[0])**2 + (20+P[1])**2) + sqrt((100-P[0])**2 + (30)**2)

print(P[0])
