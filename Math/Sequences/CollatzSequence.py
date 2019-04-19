def Collatz(Input,Depth):
    DepthCounter = 0
    while DepthCounter<Depth:
        if Input == 1:
            break
        if Input%2 == 0:
            Input = Input/2
        else:
            Input=(3*Input)+1
        DepthCounter+=1     
    return int(Input)


def main():
    a = int(input("Find Collatz Sequence for: "))
    b = 0
    while Collatz(a,b)>1:
        print(b,":",Collatz(a,b))
        b+=1
    print(b,": 1")
    
    c = input("Again (Y/N): ")
    if c=="Y" or c=="y":
        main()

main()
