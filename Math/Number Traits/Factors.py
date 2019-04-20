def Factor(Number):
    for Var in range(1, int((Number ** .5) + 1)):
        if Number % Var == 0:
             print("%d x %d = %d" % (Var, (Number / Var), Number))
        Var += 1
    print("\n")
    Factor(int(input("Factor: ")))

    
Factor(int(input("Factor: ")))
               
