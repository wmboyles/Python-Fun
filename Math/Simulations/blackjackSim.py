import random


def main():

    d = 52  # Current number of cards in deck
    h = 20  # Current number of high cards in deck
    m = 12  # Current number of medium cards in deck
    l = 20  # Current number of low cards in deck
    
    Cneg2 = 0  # number of minus two hands
    Cneg1 = 0  # number of minus one hands
    C0 = 0  # number of zero hands
    C1 = 0  # number of plus one hands
    C2 = 0  # number of plus two hands
    decks = 50
    
    print ("Number of decks played: %i" % decks)
    print("0")
    
    while(decks > 0):       
        while(d > 0):
            n = random.random()
            
            Pneg2 = (float)((l * l) - l) / ((d * d) - d)
            Pneg1 = (float)(2 * m * l) / ((d * d) - d)
            P0a = (float)((m * m) - m) / ((d * d) - d)
            P0b = (float)(2 * l * h) / ((d * d) - d)
            P1 = (float)(2 * m * h) / ((d * d) - d)
            P2 = (float)((h * h) - h) / ((d * d) - d)
            
            if 0 <= n and n < Pneg2:
                Cneg2 = Cneg2 + 1
                l = l - 2
                d = d - 2
        
            elif Pneg2 <= n and n < (Pneg2 + Pneg1):
                Cneg1 = Cneg1 + 1
                l = l - 1
                m = m - 1
                d = d - 2
        
            elif (Pneg2 + Pneg1) <= n and n < (Pneg2 + Pneg1 + P0a): 
                C0 = C0 + 1
                m = m - 2
                d = d - 2
                
            elif (Pneg2 + Pneg1 + P0a) <= n and n < (Pneg2 + Pneg1 + P0a + P0b):
                C0 = C0 + 1
                l = l - 1
                h = h - 1
                d = d - 2
        
            elif (Pneg2 + Pneg1 + P0a + P0b) <= n and n < (Pneg2 + Pneg1 + P0a + P0b + P1):
                C1 = C1 + 1
                h = h - 1
                m = m - 1
                d = d - 2
        
            elif (Pneg2 + Pneg1 + P0a + P0b + P1) <= n and n < (Pneg2 + Pneg1 + P0a + P0b + P1 + P2):
                C2 = C2 + 1
                h = h - 2
                d = d - 2

            print ("%i" % abs(C2 + C2 + C1 - Cneg1 - Cneg2 - Cneg2))
            
        if d == 0 and h == 0 and l == 0 and m == 0:        
            decks = decks - 1
            d = 52  # Current number of cards in deck
            h = 20  # Current number of high cards in deck
            m = 12  # Current number of medium cards in deck
            l = 20  # Current number of low cards in deck
            print("")
            
'''    print ("Score -2 hands: %i" % Cneg2)
    print ("Score -1 hands: %i" % Cneg1)
    print ("Score 0 hands: %i" % C0)
    print ("Score 1 hands: %i" % C1)
    print ("Score 2 hands: %i" % C2)
    print ("")
    print ("Prob(-2): %f" % ((float)(Cneg2)/(Cneg2+Cneg1+C0+C1+C2)))
    print ("Prob(-1): %f" % ((float)(Cneg1)/(Cneg2+Cneg1+C0+C1+C2)))
    print ("Prob(0): %f" % ((float)(C0)/(Cneg2+Cneg1+C0+C1+C2)))
    print ("Prob(1): %f" % ((float)(C1)/(Cneg2+Cneg1+C0+C1+C2)))
    print ("Prob(2): %f" % ((float)(C2)/(Cneg2+Cneg1+C0+C1+C2)))
    
    if((2*C2+C1-Cneg1-2*Cneg2)!=0):
            print ("Error 2b: neq 0")'''

main()
