from tkinter import *
import random
import math

######################################################
def GCD(x,y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
######################################################
def Collatz(Input,Depth):
    DepthCounter = 0
    while DepthCounter<Depth:
        if Input == 1:
            break
        if Input%2 == 0:
            Input = Input/2
        else:
            Input=(3*Input)+1
        DepthCounter+=1     
    return int(Input)
######################################################
def Fibonacci(Depth):
    DepthCounter = 0
    C1 = 1
    C2 = 1
    Result=0
    while(DepthCounter<=Depth):
        Result = C1 + C2
        C1 = C2
        C2 = Result
        DepthCounter+=1
    return Result
######################################################
def IsPrime(Input):
    IsPrimeVar = 3
    if Input<2:
        return False
    if Input%2 == 0:
        return False
    while(IsPrimeVar<=pow(Input,.5)):
        if Input%IsPrimeVar == 0:
            return False
        IsPrimeVar = IsPrimeVar+2
    return True
######################################################
def PrimeNum(Depth):
    DepthP = math.fabs(Depth)
    DepthCounter = 1
    IsPrimeEntry = 3
    if DepthP == 1:
        return 2
    while DepthCounter < DepthP:
        if IsPrime(IsPrimeEntry) == True:
            DepthCounter+=1
        IsPrimeEntry+=2
    return IsPrimeEntry
######################################################
def main():
    WidthNum = int(input("Image Width: ")) #Gets image height & width
    HeightNum = int(input("Image Height: "))
    DotSize = float(input("Dot size: "))

    if(WidthNum > 1366):
        print("Width value too big. Reverting to W=1366.")
        WidthNum = 1366
    if(HeightNum > 768):
        print("Height value too big. Reverting to H=768.")
        HeightNum = 768

    canvas = Canvas(width=WidthNum, height=HeightNum) #Creates canvas window
    canvas.pack(expand=YES, fill=BOTH) #makes sure canvas is printed to screen*                

    X1 = 1 #Starting Pixel Cordinates
    Y1 = 1
    ColorTable = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    
    while (X1 != WidthNum and Y1 != HeightNum):
        if(X1%Y1==0 or Y1%X1==0):
            ColorStr = '#0123456789AB'
        elif(X1%Y1==1 or Y1%X1==1):
            ColorStr = '#123456789ABC'
        elif(X1%Y1==2 or Y1%X1==2):
            ColorStr = '#23456789ABCD'
        elif(X1%Y1==3 or Y1%X1==3):
            ColorStr = '#3456789ABCDE'
        elif(X1%Y1==4 or Y1%X1==4):
            ColorStr = '#456789ABCDEF'
        elif(X1%Y1==5 or Y1%X1==5):
            ColorStr = '#56789ABCDEF0'
        elif(X1%Y1==6 or Y1%X1==6):
            ColorStr = '#6789ABCDEF01'
        elif(X1%Y1==7 or Y1%X1==7):
            ColorStr = '#789ABCDEF012'
        elif(X1%Y1==8 or Y1%X1==8):
            ColorStr = '#89ABCDEF0123'
        elif(X1%Y1==9 or Y1%X1==9):
            ColorStr = '#9ABCDEF01234'
        elif(X1%Y1==10 or Y1%X1==10):
            ColorStr = '#ABCDEF012345'
        elif(X1%Y1==11 or Y1%X1==11):
            ColorStr = '#BCDEF0123456'
        elif(X1%Y1==12 or Y1%X1==12):
            ColorStr = '#CDEF01234567'
        elif(X1%Y1==13 or Y1%X1==13):
            ColorStr = '#DEF012345678'
        elif(X1%Y1==14 or Y1%X1==14):
            ColorStr = '#EF0123456789'
        elif(X1%Y1>=15 or Y1%X1>=15):
            ColorStr = '#F0123456789A'
        else:
            ColorStr = 'white'
  
        #ColorStr = '#%s%s%s%s%s%s%s%s%s%s%s%s'%(Color1,Color2,Color3,Color4,Color5,Color6,Color7,Color8,Color9,Color10,Color11,Color12)
        canvas.create_rectangle(X1, Y1, (X1+DotSize), (Y1+DotSize), width=0, fill=ColorStr) #Creates DotSize 'rectangles' or specified color

        if X1 == WidthNum-DotSize:
            X1 = 1
            Y1=Y1+DotSize   
        else:
            X1 = X1+DotSize

    mainloop()

    print("Image Created.")

    if input("Again: ") in ("1",'y','Y',"Yes","yes"):
        main()
    else:
        print("Program Terminated")

main()
