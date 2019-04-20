import math
import decimal
from functools import reduce


def ApproxE(n):
    return 2 + reduce(lambda x, i: x + (2 * i + 2) / math.factorial(2 * i + 1), range(n))


# Best way to approx mi
def ApproxPi(n):
    return (47 / 15) + reduce(lambda x, i: x + (1 / (16) ** i) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6))), range(n))


# Wallis product
def Wallis(n):
    return 2 * (4 / 3) * reduce(lambda x, i: x * ((2 * i) / (2 * i - 1)) * ((2 * i) / (2 * i + 1)), range(1, 2 * n))


# Leibnitz alternating sum
# It's bad: Leibnitz(1000)+.001 is better and faster than Leibnitz(100000)
def Leibnitz(n):
    return 4 + reduce(lambda x, i: x + 4 * ((-1) ** i) / (2 * i + 1), range(n))


# Sum for pi based on solution to Basel problem
# 1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ... = (pi^2)/6
def Basel(n):
    return math.sqrt(reduce(lambda x, i: x + 6 / i ** 2, range(n)))


def IntrestE(n):
    return (1 + 1 / n) ** n


def getBestPi(dem):
    PI = math.pi
    numr = 1
    while(numr / dem <= PI): numr += 1
    if (abs(PI - (numr / dem)) > abs(((numr - 1) / dem) - PI)): numr -= 1
    elif (abs(PI - (numr / dem)) > abs(((numr + 1) / dem) - PI)): numr += 1
    return numr
