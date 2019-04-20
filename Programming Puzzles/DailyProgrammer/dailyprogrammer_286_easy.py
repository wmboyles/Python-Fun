from math import sqrt

factDiv = factorial = int(input("Reverse Factorial: "))
for i in range(2, int(sqrt(factorial)) + 3):
    if factDiv == 1:
        print(str(factorial) + " = " + str(i - 1) + "!")
        break
    if factDiv % i == 0: factDiv /= i
    else:
        print("NONE")
        break
input()  # This line is only nessary to see output outside of IDLE        
        
