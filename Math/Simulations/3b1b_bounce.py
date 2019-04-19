d=int(input("Digits: "))

print("i-m1-collisions")
for i in range(1,10**d+1):
    m1 = i**2
    m2 = 1

    u1 = 1
    u2 = 0

    collision_count = 0
    i=0

    while(u1>u2):
        v1 = u1*(m1-m2)/(m1+m2) + u2*(2*m2)/(m1+m2)
        v2 = u2*(m2-m1)/(m1+m2) + u1*(2*m1)/(m1+m2)
        collision_count+=2
        i+=1

        u1=v1
        u2=-v2
        #print(u1,u2)

    if(v2<0):
        collision_count-=1

    print(i,m1,collision_count)
