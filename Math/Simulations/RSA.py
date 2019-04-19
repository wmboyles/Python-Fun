import random
import math
import sys
import gc


def rabinMiller(n):
     s = n-1
     t = 0
     while s%2 == 0:
         s = s/2
         t+=1
     k = 0
     while k<128:
         a = random.randrange(2,n-1)
         v = pow(a,int(s),n) #where values are (num,exp,mod)
         if v != 1:
             i=0
             while v != (n-1):
                 if i == t-1: return False
                 else:
                     i = i+1
                     v = (v**2)%n
         k+=2
     return True

def isPrime(n):
     lowPrimes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
     if (n >= 3):
         if (n%2 != 0):
             for p in lowPrimes:
                 if (n == p):
                    return True
                 if (n % p == 0):
                     return False
             return rabinMiller(n)
     return False

def generateLargePrime(k):
     #k is the desired bit length
     r=100*(math.log(k,2)+1) #number of attempts max
     r_ = r
     while r>0:
         n = random.randrange(2**(k-1),2**(k))
         r-=1
         if isPrime(n) == True:
             return n
######################################################
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
###################################################### 
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m
######################################################     
def main():
    print()
    Message = int(input("Message (integer): "))
    Prime1 = Prime2 = 0
    gc.collect()
    while Prime1==Prime2:
        Prime1 = generateLargePrime(15)
        Prime2 = generateLargePrime(15)
        
    Product = Prime1*Prime2
    Totient = (Prime1-1)*(Prime2-1)
    RelPri = Prime1+Prime2-1
    ModInv = modinv(RelPri,Totient)
    Cipher = (Message**RelPri)%Product
    #Decrypt = (Cipher**ModInv)%Product
    print("p: %s"%Prime1)
    print("q: %s"%Prime2)
    print("n: %s"%Product)
    print("t: %s"%Totient)
    print("e: %s"%RelPri)
    print("d: %s"%ModInv)
    print("Private Key: (%s,%s)"%(ModInv,Product))
    print("Public Key: (%s,%s)"%(RelPri,Product))
    print("Cipher: %s"%Cipher)
    print("Decrypt: %s"%Message)#make this faster so it can be asctuaaly used
    again = input("Again (Y/N): ")
    if again is 'y' or again is 'Y': main()
######################################################
main()
