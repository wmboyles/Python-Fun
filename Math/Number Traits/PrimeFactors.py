def Factor(Number):
    for Var in range(2,int((Number**.5)+1)):
        if Number%Var==0:
             return Var
    return False


def main():
    Number = int(input("Factor: "))
    print("%i = ..."%Number)
    while Factor(Number)!=False:
        print("%i x"%Factor(Number))
        Number = Number/Factor(Number)
    print(int(Number))
    Again = input("Again(Y/N): ")

    if(Again == "Y" or Again == "y"):
        print("------------------------------")
        main()
    else:
        return 0

def PFCount(Number):
    Factors=0
    while Factor(Number)!=False:
        Factors=Factors+1
        Number = Number/Factor(Number)
    return Factors+1

main()
