import math
import random

#All of these produce floats with 4 digits of precision

''' The Middle Square algorithm is credited to John Von Neuyman. It produces
    pseudo-random numbers. All pseudo-random numbers eventually repeat in in the
    same sequence. This means that the same input alwys gives the same output.
    All sequences generated with this algorithm will always cycle back with a
    period less than 4096 if the range is [0,9999]
'''
def MiddleSquare(seed, amount):     #Von Neuyman's Middle Square Algorithm (ish)
    for i in range(0,amount):
        length = int(math.log10(seed))+1
        seed = seed**2
        lengthSquare = int(math.log10(seed))+1
        seed = (seed-1000000*math.floor(seed/1000000)-(seed%100))/100 #gets middle 4 digits
        print(int(seed))

''' The Linear Coungrential generator produces pusedo-random numbers using four inputs.
    Although the resulting outputs are pretty even desitrubuted, this method is not perfect.
    For example, put in LinCongGen(10000,300,2310,4321,1000) and you will get 9 5310's
    and one 8610 at the beginning. Also, even when using different, seemingly more random
    parameters, the outputs will follow cyclical patterns that can make some ranges
    occur much more frequently. For exmaple LinCongGen(10000,378,2310,4321,10000) is much
    more likely to produce numbers between 300 and 400 than 500 and 600. Also, the mean
    will generally not go to m/2 as the number of outputs increases.

    If we select "good" values for m, a, and c, the period of sequences will be m.
    LCG sequences tend to have larger periods than Middle Square sequences.
'''

def LinCongGen(m, a, c, seed, amount): #Linear Congruential Generator
    number=0
    for i in range(0,amount):
        seed = (seed*a+c)%m
        print(seed)


seed = int(input("Seed: "))        
print("==============================================")
random.seed(seed)
print("Python Random")
print(random.randint(0,9999))
print("==============================================")
print("Middle Square")
MiddleSquare(seed,1)
print("==============================================")
print("Linear Congruential Generator")
LinCongGen(10000,378,2310,seed,1)
print("==============================================")
input("ENTER to EXIT")
