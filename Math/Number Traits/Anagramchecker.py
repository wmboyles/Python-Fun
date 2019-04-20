def isAnagram():
    A1 = str(input("Anagram phrase 1: "))
    A2 = str(input("Anagram phrase 2: "))

    L1 = list(''.join(e for e in A1 if(e.isalnum())))
    L2 = list(''.join(e for e in A2 if(e.isalnum())))

    if len(L1) != len(L2): return False
    
    L1.sort()
    L2.sort()

    for i in range(len(L1)):
        if L1[i] != L2[i]: return False
    return True


def isAnagram2():
    A1 = str(input("Anagram phrase 1: "))
    A2 = str(input("Anagram phrase 2: "))

    L1 = list(A1.lower().replace(" ", "").replace(":", "").replace(";", "").replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("'", "").replace("\"", "").replace("-", ""))
    L2 = list(A2.lower().replace(" ", "").replace(":", "").replace(";", "").replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("'", "").replace("\"", "").replace("-", ""))

    R1 = [5, 71, 37, 29, 2, 53, 59, 19, 11, 83, 79, 31, 43, 13, 7, 67, 97, 23, 17, 3, 41, 73, 47, 89, 61, 101]
    
    Product1 = 1
    Product2 = 1

    for i in range(0, len(L1)):
        Product1 = Product1 * R1[(ord(L1[i]) - 97)]

    for i in range(0, len(L2)):
        Product2 = Product2 * R1[(ord(L2[i]) - 97)]

    if(Product1 == Product2): return True
    else: return False


if __name__ == '__main__':
    print(isAnagram2())
