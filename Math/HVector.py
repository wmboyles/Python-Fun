'''
input: 5 10 10 5
triangle:
     1
    1 5
   1 4 10
  1 3 6 10
 1 2 3 4 5
1 1 1 1 1
'''
from math import factorial
from random import randint
def hVector(inp): #inp is list
    delDiag=[]
    hVector=[]
    #Fill w/ 1's
    for i in range(len(inp)+2): delDiag.append(1)
    hVector.append(delDiag[-1])

    #Compute Vector
    for i in range(len(inp)):
        delDiag[0]=inp[i]
        subNum=inp[i]
        
        for j in range(1,len(delDiag)):
            delDiag[j] = subNum - delDiag[j]
            subNum = delDiag[j]
            
        del delDiag[-1] 
        hVector.append(delDiag[-1])
        
    return hVector

def isPalindronic(l): return l==l[::-1]

def choose(n,k): return factorial(n)//(factorial(k)*factorial(n-k))

#minDim=2 and maxDim=5 would check from a 2-simplex(tetrahedron) to a 5-simplex
#Simplexes 1 (minDim) to 2000 (maxDim) checked
#Conjecture the h-vector of an n-simplex is all 1's
def checkSimplexes(minDim,maxDim):
    for dim in range(minDim,maxDim):
        #make random simplex
        simplex=[dim+2]
        for j in range(dim): simplex.append(choose(simplex[0],j+2))
        hVec = hVector(simplex)
        if not isPalindronic(simplex): print(simplex)

                                                             
