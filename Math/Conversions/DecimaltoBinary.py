def decToBin(n):
    out = ""
    if(n == 0): out = "0"
    while(n >= 1):
        out += str(n % 2)
        n = int((n - n % 2) / 2)
    return out[::-1]


def main():
    print("Binary: %s" % (decToBin(int(input("Decimal: ")))))
    a = input("Again: ").lower()
    if(a[0] == 'y' or a == '1'): main()


main()
    
