import numpy as np

def LatinSquare():
    possible = np.array([[1,2,3,4,5],[5,1,2,3,4],[4,5,1,2,3],[3,4,5,1,2],[2,3,4,5,1]])
    checker1 = np.array([[1,2,3,4,5]])
    checker2 = np.array([[1],[2],[3],[4],[5]])
    print(possible)
    
    for i1 in range(0,int(pow(possible.size,.5))-1):
        for i2 in range(0,int(pow(possible.size,.5))-1):
            if(possible[i1,i2] in checker1):
                checker1 = checker1[checker1!=possible[i1,i2]]
            else:
                return False
            if(possible[i2,i1] in checker2):
                checker2 = checker2[checker2!=possible[i2,i1]]
            else:
                return False
            
        checker1 = np.array([[1,2,3,4,5]])
        checker2 = np.array([[1],[2],[3],[4],[5]])
        
    return True

print(LatinSquare())
