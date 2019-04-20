from math import sqrt, floor

# Solve Pell's equation algorithmically
# x^2 - Sy^2 = 1


def Pell(S):
    if(sqrt(S) == floor(sqrt(S))): return [1, 0]

    N = [0, 1, floor(sqrt(S))]
    a0, p = N[2], 0
    contFrac = [a0]

    while(N[2] != 2 * a0):
        N[0] = (N[1] * N[2]) - N[0]
        N[1] = (S - (N[0] ** 2)) // N[1]
        N[2] = floor((a0 + N[0]) / N[1])
        contFrac.append(N[2])
        p += 1

    A, B = [1, a0], [0, 1]

    if(p % 2 == 1): contFrac = contFrac + contFrac[1:]

    for i in range(1, (1 + p % 2) * p):
        A = [A[1], contFrac[i] * A[1] + A[0]]
        B = [B[1], contFrac[i] * B[1] + B[0]]

    return [A[1], B[1]]


# Solves x^2 - Sy^2 = -S
# X value will be a multiple of S
def alteredPell(S):
    Y = Pell(S)[0]
    X = int(sqrt(S * (Y ** 2 - 1)))
    return [X, Y]


# Used for calculating generating function
def Pell2(S):
    if(sqrt(S) == floor(sqrt(S))): return [1, 0]
    N = [0, 1, floor(sqrt(S))]
    a0, p = N[2], 0
    contFrac = [a0]
    while(N[2] != 2 * a0):
        N[0] = (N[1] * N[2]) - N[0]
        N[1] = (S - (N[0] ** 2)) // N[1]
        N[2] = floor((a0 + N[0]) / N[1])
        contFrac.append(N[2])
        p += 1
    A, B = [1, a0], [0, 1]
    for i in range(1, p):
        A = [A[1], contFrac[i] * A[1] + A[0]]
        B = [B[1], contFrac[i] * B[1] + B[0]]
    return [A[1], B[1]]


# Calculates "Generating Function" for sqrt(S) continued fraction
def contFPG(S):
    A, C = Pell2(S)
    B, D = S * C, A
    print("{0}x+{1}".format(A, B))
    print("------")
    print("{0}x+{1}".format(C, D))


# Gets continued fraction of sqrt(D)
def contFrac(D):
    a0 = floor(sqrt(D))
    aNew = a0
    i = 0
    p = [a0]
    q = [1]
    a = [a0]

    while a[-1] != 2 * a0:
        p.append(a[i] * q[i] - p[i])
        q.append((D - (p[i + 1] ** 2)) / q[i])
        a.append((floor((a0 + p[i + 1]) / q[i + 1])))
        if aNew == 2 * a0: break
        i += 1
        
    return a[2:]
