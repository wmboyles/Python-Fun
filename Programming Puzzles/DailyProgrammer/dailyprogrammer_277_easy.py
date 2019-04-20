from math import gcd


def SimplifyFraction(x, y): print(str(x) + '/' + str(y) + ' = ' + str(x // gcd(x, y)) + '/' + str(y // gcd(x, y)))
