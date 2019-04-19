#Main puzzle
def generalizedIE(word,char):
    if "ei" not in word and "ie" not in word: return True

    elif "ei" in word:
        if (char+"ei") in word: return True
        else: return False
    
    elif "ie" in word:
        if (char+"ie") not in word: return True
        else: return False


#Bonus 1
def checkList():
    with open("enable1.txt",'r') as l:
        return sum(not generalizedIE(word[:-1],"c") for word in l)


#Bonus 2
def checkAll():
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    minimalExceptions, minExceptChar = 9999, "c"
    for char in alphabet:
        with open("enable1.txt",'r') as l:
            exceptions = sum(not generalizedIE(word[:-1],char) for word in l)
            print(char,exceptions)
