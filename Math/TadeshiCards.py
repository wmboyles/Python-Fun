from math import gcd
from functools import reduce

def GCD(L):
    if len(L)>2:
        newL = [gcd(L[0],L[1])]+L[2:]
        return GCD(newL)
    else: return gcd(L[0],L[1])

def multAll(L): return reduce(lambda x,y: x*y,L)

def LCM(L): return reduce(lambda x,y: (x*y)//gcd(x,y),L,1)

def main():
    MAX = int(input("Cards: "))
    print(LCM(list(range(2,MAX+1)))-1)
    main()
