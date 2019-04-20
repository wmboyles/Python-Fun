import random
import numpy as np


def main():
    triples = 0
    trials = int(input("Trials: "))
    seen1 = set()
    seen2 = set()
        
    for i in range(1, trials):
        Room = [random.randint(1, 365) for i in range(30)]

        seen1.clear()
        seen2.clear()
        
        for b in Room:
            if b in seen2:
                triples += 1
                break
            elif b in seen1:
                seen2.add(b)
            else:
                seen1.add(b)
                
    print(triples / trials)
    main()

    
if __name__ == '__main__': main()
