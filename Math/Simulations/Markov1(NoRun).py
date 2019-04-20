import random


def Markov(loops):
    times = int(loops)
    bull = 0
    bear = 0
    stag = 0
    stockValue = 0
    states = ["bull", "bear", "stagnant"]
    state = states[random.choice(range(0, 2))]
    for i in range(0, times):
        rand = random.random()
        if(state == "bull"):
            if rand < .9:
                state = "bull"
                bull += 1
            elif rand < .975:
                state = "bear"
                bear += 1
            else:
                state = "stagnant"
                stag += 1
        elif(state == "bear"):
            if rand < .8:
                state = "bear"
                bear += 1
            elif rand < .95:
                state = "bull"
                bull += 1
            else:
                state = "stagnant"
                stag += 1
        else:
            if rand < .5:
                state = "stagnant"
                stag += 1
            elif rand < .75:
                state = "bull"
                bull += 1
            else:
                state = "bear"
                bear += 1

    # Calculated vs predicted
    print("Bull: " + str(100 * bull / times) + "%")
    # print("Predicted: %f"%(5/8))
    print("Bear: " + str(100 * bear / times) + "%")
    # print("Predicted: %f"%(5/16))
    print("Stagnant: " + str(100 * stag / times) + "%")
    # print("Predicted: %f"%(1/16))
    print("Stock Value Change: " + str(100 * (bull - bear) / times) + "%")
    print("Predicted Change: %f" % (500 / 8 - 500 / 16) + "%")


Markov(input("Iterations: "))
