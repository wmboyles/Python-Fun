def TP1(n): return 2*n +1

def ITP1(n): return (n-1)/2

def isPosInteger(n): return n==n//1 and n!=0

def getSeries(n,N):
    series=[n]
    while TP1(series[-1])<=N: series.append(TP1(series[-1]))
    return series[1:]

def findFundamentals(N):
    fundamentals=[4,5]
    allNums=[]
    for i in range(fundamentals[-1],fundamentals[-1]+N):
        if i not in fundamentals:
            if i%2==0:
                fundamentals.append(i)
                allNums = allNums+getSeries(i,100)
            elif ITP1(i) not in fundamentals and i not in allNums:
                fundamentals.append(i)
                allNums = getSeries(i,100)
    return fundamentals


