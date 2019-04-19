from itertools import *


'''
Generates all subsets of a set, including the empty set and set itself.
If the input set has n elements, the output set will have 2**n elements.
'''
def powerset(iterable):
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))


'''
Do all subsets of a given set have unique sums?

Uncommenting the print line below will provide two subsets with the same sum.
If you also comment the return statement, it will provide all subsets with the same sums.
'''
def hasDistinctSubsetSums(item):
    itemSum = [] #the sums of all PS elements
    
    for element in powerset(item):
        s = sum(element)
        itemSum.append((s,element))

    itemSum = sorted(itemSum)
    for i in range(0, len(itemSum)-1):
        if (itemSum[i][0] == itemSum[i+1][0]) and (itemSum[i][1] != itemSum[i+1][1]):
            #print(itemSum[i][0], itemSum[i][1], "and", itemSum[i+1][1]) #counterexample
            return False

    return True


'''
Given a set of positive integers such that all subsets, have unique sums, this function
generates such a set with smaller elements by taking constant differences from the given
set.
Precondition: The input set is sorted in high-to-low order
'''
def smallerSeqCheck(item):
    if not item: return False
    
    minSeq = item
    for x in range(1,item[-1]):
        l = [i-x for i in item]
        if(hasDistinctSubsetSums(l)):
            minSeq = l

    return minSeq


'''
Attempts to construct a set beginning with a maximum starting value of a certain length
such that all subsets have unique sums.
If such a set is found, return the set.
If such a sequence can't be found, returns False.
Postcondition: Set is in high-to-low sorted order
'''
def seqConst(startingNum, numElements): #numElements = 0 returns a sequence of length 1
    l = [startingNum]
    while (len(l) < numElements+1) and l[-1]>0:
        if hasDistinctSubsetSums(l):
            if len(l) >= 3:
                l.append( l[-1] - (l[-2] - l[-1])) #this speeds things up
            else:
                l.append(l[-1]-1)
        else: #if the previously attempted element didn't work...
            l[-1]-=1

    #if len(l) <= 1:
        #return l
    if(len(l)-1 == numElements):
        return l[:-1]
    else:
        return False
