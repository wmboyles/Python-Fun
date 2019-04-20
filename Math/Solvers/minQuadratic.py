from math import gcd


# Find the Greatest Common Divisor
def GCD3(a, b, c): return gcd(gcd(a, b), c)


# Find the minimal polynomial of (h +/- sqrt(j))/k
def minQuad(h, j, k):
    A = k ** 2
    B = -2 * h * k
    C = h ** 2 - j
    H = GCD3(A, abs(B), abs(C))
    return [A // H, B // H, C // H]


# Arrange results of minQuad into a string
def main(p=True):
    if p: print("\nMinimal Parabolic of (h +/- sqrt(j))/k")
    else: print()
    
    A, B, C = minQuad(int(input("h: ")), int(input("j: ")), int(input("k: ")))
    
    if A == 1: out = "x^2"
    else: out = "{}x^2".format(A)
    
    if B <= 1:
        if B is 1: out += " + x"
        elif B == -1: out += " - x"
        elif B < 0: out += " - {}x".format(abs(B))
        # If B is 0 don't add anything
    else: out += " + {}x".format(B)

    if C <= 0:
        if C < 0: out += " - {}".format(abs(C))
        # If C is 0 don't add anything
    else: out += " + {}".format(C)

    print(out)

    again = input("Again (Y/N): ") 
    if again == 'y' or again == 'Y': main(False)


main()
