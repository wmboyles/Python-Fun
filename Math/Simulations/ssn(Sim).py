import random

# How many people need to be in a class before there is a 50% chance that at least two people have
# the same last 4 digits of their SSN?
    # Assume digits are randonly assigned

# ANSWER -- 119


# Returns a random 4-digit number as from "0000" to "9999"
def rand4():
    long = "000" + str(random.randint(0, 9999))
    short = long[len(long) - 4:]
    return short


def makeList(listLen):
    numList = []
    for i in range(listLen):
        numList.append(rand4())
    return numList


def anyRepeats(numList):
    return len(set(numList)) != len(numList)
    
        
def prop(size, trials):
    # size = int(input("Class Size: "))
    # trials = int(input("Trials: "))
    numDupeCount = 0
    for i in range(trials):
        if anyRepeats(makeList(size)) is True: numDupeCount += 1
    return numDupeCount / trials
    # main(size,trials)
