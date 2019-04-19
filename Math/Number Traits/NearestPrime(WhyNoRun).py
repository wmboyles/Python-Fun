from math import sqrt

def IsPrime(Possible):        #Tells if number is prime or not
    if(Possible==2):
        return True
     
    if(Possible <2 or Possible%2==0 or Possible%5==0):
        return False
    
    for x in range(3, int(sqrt(Possible)+.5),2):
        if Possible % x == 0:
            return False

    return True

def NearestPrimes(n):
    p1=n
    p2=n
    
    if(IsPrime(n)==True):
        print("%i is prime."%n)
    else:
        if(n%2==0):
            p1-=1
            p2+=1
        else:
            p1-=2
            p2+=2
        while(not IsPrime(p1)):
            p1-=2
        while(not IsPrime(p2)):
            p2+=2
        print("%i < %i < %i"%(p1,n,p2))

inputList = [270,541,993,649,2010741] #Can't do 1425172824437700148 in good time.
for inp in inputList: NearestPrimes(inp)

'''Note: How can we implement Miller-Rabin?'''
