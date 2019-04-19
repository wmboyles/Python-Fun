#In the string "ABBA" A recurs first b/c A happens first
def Recurring1(inp):
    for i in range(len(inp)):
        if inp[i] in inp[i+1:]:
            return inp[i],i
    return "None"

#In the string "ABBA" B is recurs first b/c B has the first match along the inp
def Recurring2(inp):
    uniques = set()
    for char in inp:
        if char in uniques:
            return char, inp.find(char)
        uniques.add(char)


print(Recurring1(input()))
print(Recurring2(input()))
