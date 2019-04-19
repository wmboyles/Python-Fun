from tkinter import *
import random

def main():
    WidthNum = int(input("Image Width: ")) #Gets image height & width
    HeightNum = int(input("Image Height: "))
    DSN = int(input("Dot size: "))

    if(WidthNum > 1366):
        print("Width value too big. Reverting to W=1366.")
        WidthNum = 1366
    if(HeightNum > 768):
        print("Height value too big. Reverting to H=768.")
        HeightNum = 768

    canvas = Canvas(width=WidthNum, height=HeightNum) #Creates canvas window
    canvas.pack(expand=YES, fill=BOTH) #makes sure canvas is printed to screen*                

    X1 = 0 #Pixel Cordinates
    Y1 = 0
    ColorTable = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    
    while (X1 != WidthNum and Y1 != HeightNum):
        Color1 = str(ColorTable[random.randint(0,1000000)%16])
        Color2 = str(ColorTable[random.randint(0,1000000)%16])
        Color3 = str(ColorTable[random.randint(0,1000000)%16])
        Color4 = str(ColorTable[random.randint(0,1000000)%16])
        Color5 = str(ColorTable[random.randint(0,1000000)%16])
        Color6 = str(ColorTable[random.randint(0,1000000)%16])
        Color7 = str(ColorTable[random.randint(0,1000000)%16])
        Color8 = str(ColorTable[random.randint(0,1000000)%16])
        Color9 = str(ColorTable[random.randint(0,1000000)%16])
        Color10 = str(ColorTable[random.randint(0,1000000)%16])
        Color11 = str(ColorTable[random.randint(0,1000000)%16])
        Color12 = str(ColorTable[random.randint(0,1000000)%16])
        ColorStr = '#%s%s%s%s%s%s%s%s%s%s%s%s'%(Color1,Color2,Color3,Color4,Color5,Color6,Color7,Color8,Color9,Color10,Color11,Color12)

        canvas.create_rectangle(X1, Y1, (X1+DSN), (Y1+DSN), width=0, fill=ColorStr) #Creates one pixel 'rectangles' or specified color
            
        if X1 == (WidthNum-DSN):
            X1 = 0
            Y1 = Y1+DSN  
        else:
            X1 = X1+DSN  

    mainloop()

    print("Image Created.")

main()

if int(input("Again: "))==1:
    main()
else:
    print("Program Terminated")
