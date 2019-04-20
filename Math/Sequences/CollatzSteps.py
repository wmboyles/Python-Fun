def main():
    print("Num | Steps")
    for n in range(0, 1000000):
        inp = n        
        steps = 0
        while inp > 1:
            if(inp % 2 == 0):
                inp = inp / 2
            else:
                inp = (3 * inp) + 1
            steps += 1
        print("", n, " : ", steps)


input("ENTER TO START")
main()
