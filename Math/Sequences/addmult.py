n = int(input("n: "))
a = 0
for x in range(0, n + 1):
    if(x & 1):
        a = a + x
    else:
        a = a * x
    print("%i %i" % (x, a))
input("Press ENTER to continue... ")
