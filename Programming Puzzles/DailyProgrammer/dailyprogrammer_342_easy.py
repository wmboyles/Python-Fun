import numpy as np

def PrintPoly(cofs):
    power = len(cofs)-1
    out=""
    S="+"
    X="x^"
    Power=power
    
    for cof in cofs:
        if(cof<=0 or power==len(cofs)-1): S=""
        else: S="+"
        
        if(power==0):
            X=""
            Power=""
        elif(power==1):
            X="x"
            Power=""
        else:
            X="x^"
            Power=str(power)

        out+=S+str(cof)+X+Power+" "

        power-=1
        
    return out

def PolyDiv(cofs1,cofs2):
    div = np.polydiv(cofs1,cofs2)
    print("Quotient: "+PrintPoly(div[0]))
    print("Remainder: "+PrintPoly(div[1]))


a = np.array([10,0,-7,0,-1])
b = np.array([1,-1,3])
PolyDiv(a,b)
