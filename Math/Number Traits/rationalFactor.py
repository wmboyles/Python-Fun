from math import sqrt
from fractions import Fraction
from decimal import Decimal

def decFactor(s):
    frac = Fraction(Decimal(s))
    #print("(")
    factor(frac.numerator)
    print("/")
    factor(frac.denominator)
    #print(")")
    
def getFactor(n):
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0: return i
    return False

def factor(n):
    fact = getFactor(n)
    while fact!=False:
        print("{} x".format(fact))
        n//=fact
        fact = getFactor(n)
    print(n)

def main():
    print("Factor a non-integer rational")
    decFactor(input("Number: "))
    again = input("Again (Y/N): ")
    if again=='y' or again=='Y': main()

main()
