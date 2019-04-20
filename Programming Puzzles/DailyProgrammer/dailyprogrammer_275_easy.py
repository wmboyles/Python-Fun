def isValidElement(fullName, abbr):
    if(len(abbr) != 2): return False  # Rule 1
    
    if(abbr[0].lower() not in fullName.lower() or abbr[1].lower() not in fullName.lower()): return False  # Rule 2

    firstLetter = 0
    
    for i in range(0, len(fullName)):  # For loops do rules 3 and 4
        if fullName.lower()[i] == abbr[0]:
            firstLetter = i
            break
        
    for i in range(firstLetter + 1, len(fullName)):
        if fullName.lower()[i] == abbr[1]: return True

    return False


def getValidName(element):  # Bonus 1
    validElements = []
    
    for i1 in range(0, len(element)):
        for i2 in range(i1, len(element)):
            if ord(element[i1].lower()) <= ord(element[i2].lower()) and isValidElement(element, element[i1].upper() + element[i2].lower()):
                validElements.append(element[i1].upper() + element[i2].lower())

    bestElement = validElements[0]
    for abbr in validElements:
        if(ord(abbr[0]) < ord(bestElement[0])): bestElement = abbr
        if(ord(abbr[0]) == ord(bestElement[0])):
            if(ord(abbr[1]) < ord(bestElement[1])): bestElement = abbr

    return element + ": " + bestElement


def validAbbrs(element):  # Bonus 2
    validAbbrs = set()

    for i1 in range(0, len(element)):
        for i2 in range(0, len(element)):
            if isValidElement(element, element[i1].upper() + element[i2].lower()):
                    validAbbrs.add(element[i1].upper() + element[i2].lower())

    return element + ": " + str(len(validAbbrs)) + " ways"


element = input("Element: ")
abbr = input("Abbreviation: ")
print("Valid Abbreviation: " + str(isValidElement(element, abbr)))
print(getValidName(element))
print(validAbbrs(element))
