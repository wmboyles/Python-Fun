def Fibonacci(Depth):
    if(Depth in (0, 1)): return 1
    DepthCounter = 2
    C1 = C2 = 1
    Result = 0
    while(DepthCounter <= Depth):
        Result = C1 + C2
        C1 = C2
        C2 = Result
        DepthCounter += 1
    return Result


def main():
    print("\nNumber of digits in Nth Fibonacci number")
    a = int(input("N: "))
    for x in range(0, a):
        FibonacciFile = open("b000045.txt", "a")
        FibonacciFile.write(str(x + 1) + " " + str(Fibonacci(x)) + '\n')
        FibonacciFile.close()
        # print(str(x+1)+" "+str(Fibonacci(x)))
    print("Length: " + str(len(str(Fibonacci(x)))) + " digits")
    if input("Again (Y/N): ") == 'y' or 'Y': main()


main()
    
