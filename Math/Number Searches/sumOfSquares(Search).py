def IsPrime(Possible):  # Tells if number is prime or not
    if(Possible <= 1):
        return False
    j = Possible ** (.5)
    i = 2
    while(i <= j):
        if(Possible % i == 0):
            return False
        if i == 2:
            i = 3
        else:
            i += 2
    return True


def main():
    x = 0
    y = 0

    for y in range (0, 251):  # y goes from 0 to 100 inclusive
        for x in range(0, 251):  # x goes from 0 to 100 inclusive
            n = (((x) ** 2) + ((y) ** 2))
            if(IsPrime(n) == True):
                if(IsPrime((((x - 1) ** 2) + ((y - 1) ** 2))) == False):
                    if(IsPrime((((x + 1) ** 2) + ((y - 1) ** 2))) == False):
                        if(IsPrime((((x - 1) ** 2) + ((y + 1) ** 2))) == False):   
                            if(IsPrime((((x + 1) ** 2) + ((y + 1) ** 2))) == False):
                                print(n)
        x = 0


main()
    
