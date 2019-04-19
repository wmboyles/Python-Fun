from math import floor
def Sqrt(number, decimals):
    answer = (1+number)/2
    for i in range(0,100):
        answer = (answer+(number/answer))/2
    answer = floor(answer*pow(10,decimals))/(pow(10,decimals))
    print(answer)


Sqrt(12345678901234567890123456789,1)

'''
The method given is a dumb way to do square roots manually.
This method uses newtown's square root with 100 iterations.
'''
