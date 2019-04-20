def String2Num(s):
    List = list(s)  # converts string to character list: AB = {'A','B'}
    Output = []  # declares Output as list

    for count1 in range(0, len(s)):
        Output.append(ord(List[count1]))  # ord(%c) returns ASCII char code

    print("ASCII: " + str(Output).strip('[]'))  # prints list without ['s and ]'s
    return Output


def Num2String(s):  # converts list of ints to string
    Output = []
    
    for count1 in range(0, len(s)):
        Output.append(chr(s[count1]))

    print("Converted Back: " + ''.join(Output))


def main():
    Num2String(String2Num(str(input("Input: "))))
    Again = input("Again: ")
    if Again in ("Yes", "y", "Y", "1", "yes"):
        main()
    if Again in ("No", "n", "N", "0", "no"):
        raise exit(0)

    
main()
