import random

avg = 0
for a in range(0, 10000):
    prod = 1
    for i in range(0, 500):
        rand = random.random()
        if rand > 0.00001 or rand < 0.99999:
            prod *= rand
    avg += pow(prod, 1 / 500)
avg /= 10000
print(avg)
