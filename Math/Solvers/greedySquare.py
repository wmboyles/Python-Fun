# Gives number of squares to make an axb grid
# at each step the largest square(s) possible are taken
def greedySquare(a, b):
    if b == 0:
        print("Smallest sidelength: {}".format(a))
        return 0
    elif b > a: return (b // a) + greedySquare(a, b % a)
    else: return (a // b) + greedySquare(b, a % b)


def main():
    print("\nGREEDY SQUARE of AxB restangle")
    out = str(greedySquare(int(input("A: ")), int(input("B: "))))
    print(out + " squares")
    main()


main()
    
