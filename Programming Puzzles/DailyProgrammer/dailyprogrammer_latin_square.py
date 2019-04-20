    import numpy as np


def isLatinSquare():
	possible = np.array([[1, 3], [3, 4]])
	checker1 = checker2 = np.arange(1, int(possible.size ** .5) + 1)
	checker2 = checker2.reshape(int(possible.size ** .5), 1)
	if(np.shape(possible)[0] != np.shape(possible)[1]): return False
	for i1 in range(0, int(pow(possible.size, .5))):
		for i2 in range(0, int(pow(possible.size, .5))):
			if(possible[i1, i2] in checker1): checker1 = checker1[checker1 != possible[i1, i2]]
			else: return False  
			if(possible[i2, i1] in checker2): checker2 = checker2[checker2 != possible[i2, i1]]
			else: return False        
		checker1 = checker2 = np.arange(1, int(possible.size ** .5) + 1)
		checker2 = checker2.reshape(int(possible.size ** .5), 1)
	return possible[np.argsort(possible[:, 0])]  # Thanks /u/tomekanco for helping me learn


print(isLatinSquare())
