import random
def Markov(loops):
    times = int(loops)
    cloud=0
    rain=0
    sun=0
    climate = ["cloud","rain","sun"]
    state = climate[random.choice(range(0,2,1))]
    for i in range(0,times):
        rand = random.random()
        if(state=="cloud"):
            if rand<.1:
                state="cloud"
                cloud+=1
            elif rand<.6:
                state="rain"
                rain+=1
            else:
                state="sun"
                sun+=1
        elif(state=="rain"):
            if rand<.6:
                state="rain"
                rain+=1
            elif rand<.9:
                state="cloud"
                cloud+=1
            else:
                state="sun"
                sun+=1
        else:
            if rand<.5:
                state="sun"
                sun+=1
            elif rand<.9:
                state="cloud"
                cloud+=1
            else:
                state="rain"
                rain+=1
                
    #Calculated vs predicted
    print("Sunny: "+str(100*sun/times)+"%")
    print(21/69)
    print("Cloudy: "+str(100*cloud/times)+"%")
    print(19/69)
    print("Rainy: "+str(100*rain/times)+"%")
    print(29/69)

Markov(input())
