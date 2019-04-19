def IsPrime(Possible):        #Tells if number is prime or not
    if(Possible <=1):
        return False
    x = Possible**(.5)
    i=2
    while(i<=x):
        if(Possible%i==0):
            return False
        if i==2:
            i=3
        else:
            i+=2
    return True

def MultipleOf(Possible):       #Tells you a prime factor of a composite number
    if(Possible==1):
        return ("no OTHER numbers besides 1")
    x = Possible**(.5)
    i=2
    while(i<=x):
        if Possible%i==0:
            return i
        if i==2:

            i=3
        else:
            i+=2  

def Options():      #For repeating program
    RepeatAns = input("Again (Y/N): ")

    if RepeatAns in {"Yes","Y","yes","y","1"}:
        main()
    elif RepeatAns in {"No","N","no","n","0"}:
        raise SystemExit #ends program
    else:
        print('Input Error')
        Options()

def main():     #main program from where functions are called
    TestNumber = int(input("Prime Test: "))
    
    if IsPrime(TestNumber)==True:
        print("%d is prime."%TestNumber)
    else:
        Divisor = MultipleOf(TestNumber)
        print("%d is composite. It is divisible by %s"%(TestNumber,Divisor))

    Options()

main()
