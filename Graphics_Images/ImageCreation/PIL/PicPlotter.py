from PIL import Image
from ctypes import windll, Structure, c_long, byref
from random import randint
from math import sqrt, fabs, gcd

'''
Plotter.py
By: William Boyles

This program creates bitmaps of a given size using equations for R, G, and B
of each pixel's RGB value. The functions below help give some cool effects.
I would recommend using x and y in some way as parameters for R, G, and B.
Many of these functions need to be optimized to run faster, especially for large
images (Desktop resolution and higher). Feel free to speed up this program add
add your own functions in.
'''


def Factor(n):  # Returns smallest factor
    for v in range(2, int(sqrt(n) + 1)):
        if Number % v == 0: return v
    return False


def PFCount(n):  # Returns number of prime factors
    factors = 1
    while Factor(n) != False:
        factors += 1
        n = n / Factor(n)
    return factors

    
def GetPixelRGB(x, y):  # returns RGB value of a certain position in the image -- SLOW
    im = Image.open("img1.bmp")
    pix = im.load()
    return pix[x, y]


def IsPrime(Input):  # Tells if a number is prime
    IsPrimeVar = 3
    if Input < 2:
        return False
    if Input % 2 == 0:
        return False
    while(IsPrimeVar <= pow(Input, .5)):
        if Input % IsPrimeVar == 0:
            return False
        IsPrimeVar = IsPrimeVar + 2
    return True


def PrimeNum(n):  # Gives nth prime number
    DepthP = fabs(n)
    DepthCounter = 1
    IsPrimeEntry = 3
    
    if DepthP == 1: return 2
    
    while DepthCounter < DepthP:
        if IsPrime(IsPrimeEntry) == True: DepthCounter += 1
        IsPrimeEntry += 2
        
    return IsPrimeEntry


def Fibonacci(n):  # Gives nth fibonacci number 
    if(n in (0, 1)): return 1
    
    DepthCounter = 2
    C1 = C2 = 1
    Result = 0

    while(DepthCounter <= n):
        Result = C1 + C2
        C1, C2 = C2, Result
        DepthCounter += 1
        
    return Result


def Collatz(n, d):  # Returns dth number in Collatz sequence for n
    steps = 0
    
    while steps < d and n != 1:
        if n % 2 == 0: n = n / 2
        else: n = (3 * n) + 1
        
        steps += 1
        
    return int(n)


def GCD(a, b):  # Gives GCD of x and y
    return gcd(a, b)


def LCM(a, b):  # Gives LCM of x and y
    return (a * b) / (gcd(a, b))


def eGCD(a, b):  # Extended GCD: A Helper Function for ModInv
    if a == 0: return (b, 0, 1)
    
    g, y, x = eGCD(b % a, a)

    return (g, x - (b // a) * y, y)


def modInv(a, m):  # Gives b such that ab=1(mod m)
    g, x, y = eGCD(a, m)
    
    if g != 1: return False  # There's is no modular inverse if this happens
    
    return x % m


class POINT(Structure):  # Helper clas for MousePos()
    _fields_ = [("x", c_long), ("y", c_long)]

    
def MousePos():  # Returns a tuple (x,y) for cursor position
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    pos = (pt.x, pt.y)

    return pos
# To trace out the path of the mouse, make r=g=b=255 and do pixs[MousePos()[0],MousePos()[1]] = (int(r),int(g),int(b)) 


def geoMean(l):
    gMean = 1
    for i in l: gMean *= i
    gMean = gMean ** (1 / len(l))
    return gMean


def mean(l): return sum(l) / len(l)

#################################################################################################################################################################'


def main(filename='xxx.bmp', size=(1920, 1080)):
    x = y = 0
    r = g = b = 0

    img = Image.new('RGB', size)
    width, height = size
    pix = img.load()

    while y != height:
        for x in range(0, width):
            r = 255
            g = 255
            b = 255
            
            pix[x, y] = (int(r), int(g), int(b))
            
            if x == width - 1:
                x, y = 0, y + 1
                if y % 10 == 0 or y == height: print(y)
                    
    img.save(filename)
    img.show()
    

main()
