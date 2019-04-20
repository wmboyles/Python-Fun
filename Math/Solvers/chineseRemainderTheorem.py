from math import gcd
from functools import reduce

# This program Solves any linear system of congruences for which the moduli are co-prime.


# Checks if all elements of a list are coprime with each-other
def pairwiseCoprime(l):
    return not any(gcd(I, J) != 1 for i, I in enumerate(l) for J in l[i + 1:])

    
def simplify(L):
    if len(L) == 2: return L
    if len(L) == 4: L = [L[0], (L[2] - L[1]) % L[3], L[3]]
    
    # Find L[0]*i such that L[0]*i = L[1] (mod L[2])
    for i in range(1, L[2]):
        if (L[0] * i) % L[2] == L[1]: return [i % L[2], L[2]]
        
    return [L[1], L[2]]

   
def CRT(inp):
    inp = [simplify(L) for L in inp]  # Simplify each item in system
    secondProd = reduce(lambda x, y: x * y, [item[1] for item in inp])  # Product of moduli

    if not pairwiseCoprime([L[1] for L in inp]): return False  # No Solution

    ans = [secondProd // i1[1] for i1 in inp]
    for j in range(len(inp)):
        ansJCopy = ans[j]
        while ans[j] % inp[j][1] != inp[j][0]: ans[j] += ansJCopy
    
    return (sum(ans) % secondProd, secondProd)  # Returns minimal solution

# [3,2,7,3] means 3x+2 = 7 (mod 3)
# [3,2,3] means 3x = 2 (mod 3)
# [2,3] means x = 2 (mod 3)


Lsys = [[1, 2], [1, 3], [1, 5], [3, 7]]
sol = CRT(Lsys)
print("{0} (mod {1})".format(sol[0], sol[1]))
input()

# EXPANSION:
    # See https://math.stackexchange.com/questions/120070/chinese-remainder-theorem-with-non-pairwise-coprime-moduli
