def isValidDate(m,d,y):
    ThirtyOneDays = [1,3,5,7,8,10,12] #Months w/ 31 days
    
    if(d<0 or d>31):
        print("Bad Day")
        return False
    elif(m==2 and d==29 and not isLeapYear(y)): return False
    elif(d==31):
        if(m not in ThirtyOneDays):
            print("NOT 31")
            return False
        
    return True


def isLeapYear(y):
    isLY=False
    if(y%4==0):
        isLY=True
        if(y%100==0):
            isLY=False
            if(y%400==0): isLY=True
    return isLY


def getMonthCode(m,y):
    MonthNums = [6,2,2,5,0,3,5,1,4,6,2,4]
    return (MonthNums[m-1]-1 if isLeapYear(y) else MonthNums[m-1])


def getYearCode(y):
    preYr = 0
    Cent = (y//100)%4
    
    if(y%100==1 or y%100==7 or y%100==12 or y%100==18 or y%100==29 or y%100==35 or y%100==40 or y%100==46 or y%100==57 or y%100==63 or y%100==68 or y%100==74 or y%100==85 or y%100==91 or y%100==96): preYr=1
    elif(y%100==2 or y%100==13 or y%100==19 or y%100==24 or y%100==30 or y%100==41 or y%100==47 or y%100==52 or y%100==58 or y%100==69 or y%100==75 or y%100==80 or y%100==86 or y%100==97): preYr=2
    elif(y%100==3 or y%100==8 or y%100==14 or y%100==25 or y%100==31 or y%100==36 or y%100==42 or y%100==53 or y%100==59 or y%100==64 or y%100==70 or y%100==81 or y%100==87 or y%100==92 or y%100==98): preYr=3
    elif(y%100==9 or y%100==15 or y%100==20 or y%100==26 or y%100==37 or y%100==43 or y%100==48 or y%100==54 or y%100==65 or y%100==71 or y%100==76 or y%100==82 or y%100==93 or y%100==99): preYr=4
    elif(y%100==4 or y%100==10 or y%100==21 or y%100==27 or y%100==32 or y%100==38 or y%100==49 or y%100==55 or y%100==60 or y%100==66 or y%100==77 or y%100==83 or y%100==88 or y%100==94): preYr=5
    elif(y%100==5 or y%100==11 or y%100==16 or y%100==22 or y%100==33 or y%100==39 or y%100==44 or y%100==50 or y%100==61 or y%100==67 or y%100==72 or y%100==78 or y%100==89 or y%100==95): preYr=6
    
    
    if(Cent==1): preYr+=5
    elif(Cent==2): preYr+=3
    elif(Cent==3): preYr+=1

    return preYr%7


def getDayName(d): return ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][d]


def dayOfWeek(m,D,y):
    M = getMonthCode(m,y)
    Y = getYearCode(y)
    dayName = getDayName((M+D+Y)%7)

    return dayName

def main():
    print("\nDay of the week of d/m/y")
    
    d,m,y = int(input("Day: ")),int(input("Month: ")),int(input("Year: "))
    
    if isValidDate(m,d,y)==False:
        input("Invalid Date.")
        main()
        
    day = dayOfWeek(m,d,y)
    
    print("{}/{}/{} is on {}".format(m,d,y,day))
    
    again = input("Again (Y/N): ")
    if again=='y' or again=='Y': main()
    
main()
