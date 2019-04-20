'''
prompt: given a list of numbers, find the largest digit that one can
obtain by concatenating the integers
ex. (1,2,3,4) -> 4321 & (9,50,432,0) -> 9504320

Leading zeroes, like 05 or 00 are not allowed
'''

import numpy as np
from math import log10, floor

challin = np.array([[420, 34, 19, 71, 341]])


def BiggestConcat1():
    firstdigit = np.zeros((1, np.size(challin)), dtype=float)
    digits = firstdigit
    elementsFD = digits
    ordered = digits
    out = ""

    for i in range(0, np.size(challin)):
        if(digits[0, i] != 0):
            digits[0, i] = floor(log10(challin[0, i]) + 1)
        else: digits[0, i] = 0

    digits = challin + digits

    for i in range(0, np.size(digits)):
        if(digits[0, i] != 0):
            moddiv = float((10 ** floor(log10(digits[0, i]))))
            firstdigit[0, i] = (digits[0, i] - digits[0, 1] % moddiv) / moddiv
        else: firstdigit[0, i] = 0

    elementsFD = np.fliplr(np.argsort(firstdigit))

    for i in range(0, np.size(challin)):
        ordered[0, i] = challin[0, elementsFD[0, i]]

    for i in range(0, np.size(ordered)):
        out += str(int(ordered[0, i]))

    print(int(out))

    
BiggestConcat1()
'''
Solution explained:

This probably isn't close to the best or most concise solution,
but it works (95% sure). I could probably shorten the code a bit
by getting rid or combining some of the arrays, but this is OK.

The solution works like this:
Loop 1) Find the number of digits in each number of our input.
        0 has 0 digits. (This will be usefull later)
        Then, add this to the inputs 
Loop 2) Find the first digit of each number and sort them so
        that you what position each element should be in
Loop 3) Order the inputs accordingly
Loop 4) Append each input to a string and print
'''
