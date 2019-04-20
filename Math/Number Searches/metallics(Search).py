from math import sin, floor, pi, sqrt


def diagonalLength(numSides, numDiams):
    return sin(pi * numDiams / numSides) / sin(pi / numSides)


def nthMetallic(n):
    return (n + sqrt(n ** 2 + 4)) / 2


def main():
    metallics = []
    for i in range(1, 10000):
        metallics.append(nthMetallic(i))

    diags = []
    for j in range(1, 1000):
        for k in range(j // 2 + 1):
            diags.append(diagonalLength(j, k))

    for metal in metallics:
        for diag in diags:
            if abs(metal - diag) < .0000001:
                print(metal, metallics.index(metal) + 1, diag)


main()
input("ENTER")
