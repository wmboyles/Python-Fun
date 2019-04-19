import random
import numpy as np

Names = np.arange(1,71)
Request = np.arange(1,71)
NR = np.zeros((70,2), dtype=int)

for i in range(0,70):
    a=Request[random.randint(0,69)]
    if(a==Request[i]):
        a=a+random.randint(1,70-a)
    NR[i]=(Names[i],a)
    NRFile = open("NR.txt", "a")
    #NRFile.write(str(NR[i,0])+'\n')
    NRFile.write(str(NR[i,1])+'\n')
    NRFile.close()
    
    
print(random.randint(0,69))
