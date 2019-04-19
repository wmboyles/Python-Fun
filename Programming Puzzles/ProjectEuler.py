import math


def isInteger(f): return int(f)==f #tells if number is an integer


def isPent(n): return isInteger((1+math.sqrt(24*n +1))/6) #tells if num is pentagonal


def isPandigital(s,n): #is string n digit pandigital
    check=[]
    for i in range(1,n+1): check+=str(i)
    return sorted(s)==check


def MultDigits(s): #Mutiplies together each digit of a string 
    out=1
    for i in range(0,len(s)): out*=int(s[i])
    return out


def isPrime(Possible):  #Tells if number is prime or not
    if(Possible==2): return True
    if(Possible <=1 or Possible%2==0): return False
    x,i = Possible**(.5),3
    while(i<=x):
        if(Possible%i==0): return False #breaks out of loop
        i+=2
    return True


def Quad(a,b,i): return (i**2 + a*i +b) #returns y=x^2 + ax + b at x=i


def d(n): #Sum of proper divisors of a number
    divs=1 #One is divisor of all nums
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            divs+=i
            if(n//i!=i): divs+=n//i #If i is divisor of n, so is n/i
    return divs


def isFactorialSum(n): #is the sum of the factorials of a numbers digits the number
    out, num = 0, str(n)
    for digit in num: out+=math.factorial(int(digit))
    return (out==n)


def Rotate(n): #keep Putting first letter of string to end until it has all cycles
    s, rotations = str(n), []
    for i in range(len(s)):
        rotations.append(int(s[1:]+s[0]))
        s = s[1:]+s[0]
    return rotations


def isPalindronic(s): #is a string palindronic // could be one liner
    l = len(s)
    return (s[:l//2 + l%2] == s[l//2:][::-1])


def decToBin(n): #deicmal to binary string
    out=""
    if(n==0): out="0"
    while(n>=1):
        out+=str(n%2)
        n=int((n-n%2)/2)
    return out[::-1]


def Trunc(s): #returns all truncations of a number(str) from the left and right
    out=[]
    for i in range(0,len(s)):
        out.append(int(s[i:]))
        out.append(int(s[:i+1]))
    del out[0] #counts orig. num twice
    return out


def Digit5th(s): return sum(int(c)**5 for c in s)==int(s)
#is sum of fifth powers of digits of a number(str) the number?


def letterToNum(c): return ord(c.lower())-96 #Returns the nth letter if the alphabet
#a/A = 1; z/Z=26


def isTriN(n): return isInteger((math.sqrt(1+8*n)-1)/2)


def isTriS(s): return isTriN(sum(letterToNum(c) for c in s))


def Factor(n): #Returns list of all prime factors of a number, putting together powers, num at end is no. of distinct factors
    primeFacts,out=[],[]
    i=2
    while(n>1):
        if n%i==0:
            if(len(primeFacts)>0 and primeFacts[-1][0]==i): primeFacts[-1][1]+=1
            else: primeFacts.append([i,1])
            n/=i
        elif(i!=2):i+=2
        else: i+=1
    if(len(primeFacts)==0): primeFacts.append([n,1])
    for ele in primeFacts: out.append(ele[0]**ele[1])
    out.append(len(out))
    return out


def getTriangle(filename): #please include .txt extension
    with open(filename) as f: triangle = f.readlines()
    triangle = [x.strip('\n').split(' ') for x in triangle]
    for num in triangle:
        for i in range(len(num)): num[i] = int(num[i])
    return triangle


import operator
def XOR(plain,key):
    out=[]
    for i in range(len(plain)):
        out.append(operator.xor(plain[i],key[i%len(key)]))
    return out


def ASCIItoStr(asciiList): #returns string that is list
    out=""
    for num in asciiList:
        try: out+=chr(num)
        except ValueError: return ""
    return out


import string
def hasAll(s):
    
    sSet = {' ',',','.','?','!','(',')',"-","/",";",":","'",'"'}
    sSet = sSet.union(string.ascii_lowercase).union(string.digits)
    d=s.lower()
    for char in d:
        if(char not in sSet): return False
    return True


def hasAdj(n): #are two letters/digits next ot each other and the same
    s=str(n)
    if(len(s)>1):
        for i in range(len(s)):
            if(s[i]==s[i+1]): return True
    return False

def digitSum(s): return sum(int(c) for c in s) #sum of digits in num


def nextApproxRoot2(num,denom):
    newNum = num+(2*denom)
    newDenom = newNum-denom
    return [newNum,newDenom]


def reverse(n): return int(str(n)[::-1])

def GCD(a,b):
    return GCD(b,a%b) if b else a

'''
This really means...
def GCD(a,b):
    if(b!=0): return GCD(b,a%b)
    else: return a

EXAMPLE
GCD(1728,1024)
1024!=0 --> GCD(1024,704)
GCD(1024,704)
704!=0 --> GCD(704,320)
GCD(704,320)
320!=0 --> GCD(320,64)
GCD(320,64)
64!=0 --> GCD(64,0)
GCD(64,0)
0==0 --> return 64
GCD(1728,1024)=GCD(1024,704)=GCD(704,320)=GCD(320,64)=GCD(64,0)=64
'''


def LCM(a,b): return int(a*(b/GCD(a,b)))


def isSquareFree(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i**2==0): return False
    return True


def reduceToSquareFree(n):
    i=2
    while(isSquareFree(n)==False):
       if(n%i==0):n//=i
       else:
           if(i!=2):i+=2
           else: i+=1
    return n


def getRootPeriod(S): #Only works for integers -- if looking for sqrt(7), S=7
    if(isInteger(math.sqrt(S))): return 0 
    nums = [0,1,math.floor(math.sqrt(S))] #m, d, a
    a0,period=nums[2],0
    while(nums[2]!=2*a0):
        mNext = (nums[1]*nums[2])-nums[0]
        dNext = (S-(mNext)**2)//nums[1]
        aNext = math.floor((a0+mNext)/dNext)
        nums = [mNext,dNext,aNext]
        period+=1
    return period


# http://mathworld.wolfram.com/PellEquation.html
def MinPell(S): #Gets minimum x,y that satisfies x^2 -Sy^2 =1 (x,y>0 and are integers)
    if(isInteger(math.sqrt(S))): return [1,0]
    
    nums = [0,1,math.floor(math.sqrt(S))] #m, d, a -- Wikipedia
    #print("Nums: {}".format(nums))

    a0, period = nums[2], 0
    #print("a0: %i"%a0)
    #print("Period: %i"%period)
    
    contFrac = [a0] #stores one period of continued fraction, including starting term
    #print("contFrac: {}".format(contFrac))
    
    while(nums[2]!=2*a0):
        mNext = (nums[1]*nums[2])-nums[0]
        dNext = (S-(mNext)**2)//nums[1]
        aNext = math.floor((a0+mNext)/dNext)
        nums = [mNext,dNext,aNext]
        #print("\nNums: {}".format(nums))
        
        contFrac.append(nums[2])
        #print("contFrac: {}".format(contFrac))
        period+=1
        #print("Period: %i"%period)
        
    A,B = [1,contFrac[0]],[0,1]
    #print("\nA: {}".format(A))
    #print("B: {}".format(B))
    
    if(period%2==1): contFrac=contFrac+contFrac[1:] #adds another period if needed to find min pell solution
    #print("contFrac: {}\n".format(contFrac))
    
    for i in range(1,(1+period%2)*period): #calculates the period*(1+period%2)th convergent of sqrt(S) --> Pell solution
        A = [A[1],contFrac[i]*A[1]+A[0]]
        B = [B[1],contFrac[i]*B[1]+B[0]]
        #print("A: {}".format(A))
        #print("B: {}\n".format(B))
    
    return [A[1],B[1]] #Pell solution


def isSmallestComb(n):
    charPrev = 0
    N = str(n)
    for i in range(1,len(N)):
        if(N[i-1]>N[i]): return False
    return True


def squareChain(n):
    seen = [n]
    nextN = 0
    while nextN not in seen:
        for char in str(n): nextN+=int(char)**2
        if nextN not in seen:
            n = nextN
            nextN=0
            seen.append(n)
        else:
            seen.append(nextN)
    return seen


def digitMultinomial(n):
    N = str(n)
    digitCount = [N.count('0')+(7-len(N)),N.count('1'),N.count('2'),N.count('3'),N.count('4'),N.count('5'),N.count('6'),N.count('7'),N.count('8'),N.count('9')]
    addNum, addDenom = math.factorial(sum(digit for digit in digitCount)), 1
    for digit in digitCount: addDenom *= math.factorial(digit)
    return addNum//addDenom


#########################################################################################################


def Euler1(n):
    total=0
    for i in range(3,n,1):
        if(i%3==0 or i%5==0): total+=i
        
    return total


def Euler2(n):
    evenSum=0
    #Get fibonacci Number
    i1=1 #0th Fibonacci Num
    i2=1 #1t Fibonacci Num 
    while i2<n:
        i1,i2 = i2,i1+i2
        if(i2%2==0): evenSum+=i2

    return evenSum


def Euler3(n):
    largestFactor=1
    if(n%2==0):
        n/=2
        largestFactor=2

    i=3
    while(n>1 and largestFactor<n):
        if(n%i==0):
            n/=i
            largestFactor=i
        else: i+=2 #This is seperate b/c numbers 27=3*3*3 would otherwise give 9

    return largestFactor


def Euler4(n):
    biggest=1
    l = 10**(n)-1-(10**(n)-1)%11 #largest multiple of 11 of n digits
    s= 11*10**(n-2) #smallest multiple of 11 of n digits
    for i1 in range(l,s,-11):
        for i2 in range(10**(n)-1,10**(n-1),-1):
            check = i2*i1
            if(check>biggest and str(check)==str(check)[::-1]):
                biggest=check
                if(str(check)[1]=='9' and str(check)[-1:]=='9'): #Does this work generally?
                    return biggest
        

def Euler5(n):
    out = 1
    for i in range(1, n+1):
        if out % i != 0: #If out doesn't divide all the numbers thus far...
            for j in range(1, n+1): #Find smallest multiple of out that divides all
                if (out*j) % i == 0:
                    out *= j
                    break
    return out


def Euler6(n):
    sumOfSquares = int(n*(n+1)*(2*n+1)/6) # =1^2+2^2+3^2+...+n^2
    squareSum = int((n*(n+1)/2))**2 # = 1+2+3+...+n
    out = squareSum-sumOfSquares
    return out


def Euler7(n):
    primeCount=2
    highestPrime=3
    while(primeCount<n):
        for i1 in range(highestPrime+2,2*highestPrime+4,2):
            for i2 in range(3,int(i1**.5)+2,1):
                if(i1%i2==0): break
                elif(i2==int(i1**.5 +1)):
                    primeCount+=1
                    highestPrime=i1
                    break
            if(primeCount==n): break
    return highestPrime


def Euler8(n):
    bigstr = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    biggest=1
    for i in range(0,len(bigstr)-n):
        prod = MultDigits(bigstr[i:i+n])#a*b*c*d*e*f*g*h*j*k*l*m*n
        if(prod>biggest): biggest=prod
    return biggest


def Euler9(n):
    for c in range(1,n):
        for b in range(1,c):
            aSqr=c**2-b**2
            a=aSqr**.5
            if(a>b): a,b=b,a
            if(int(a)==a and a+b+c==n): return int(a*b*c)
    return None


def Euler10(n):
    highestPrime=3
    primeSum=5
    while(highestPrime<n):
        for i1 in range(highestPrime+2,2*highestPrime+4,2):
            for i2 in range(3,highestPrime+1,1):
                if(i1%i2==0 or highestPrime>=n): break
                elif(i2==int(i1**.5 +1)):
                    primeSum+=i1
                    highestPrime=i1
                    break
            if(highestPrime>=n): break
        print(highestPrime)
    return primeSum-highestPrime


def Euler11():
    grid=[[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
    [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
    [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
    [52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
    [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
    [24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
    [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
    [67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
    [24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
    [21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
    [78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
    [16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
    [86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
    [19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
    [4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
    [88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
    [4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
    [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
    [20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
    [1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]

    #grid[row][column] = grid[y][x]
    biggest=1
    #Vertical Columns
    for r in range(0,17):
        for c in range(0,19):
            prod = grid[r][c]*grid[r+1][c]*grid[r+2][c]*grid[r+3][c]
            if(prod>biggest): biggest=prod

    #Horizontal Rows
    for c in range(0,17):
        for r in range(0,19):
            prod = grid[r][c]*grid[r][c+1]*grid[r][c+2]*grid[r][c+3]
            if(prod>biggest): biggest=prod

    #Left diagonals
    for r in range(3,19):
        for c in range(0,17):
            prod = grid[r][c]*grid[r-1][c+1]*grid[r-2][c+2]*grid[r-3][c+3]
            if(prod>biggest): biggest=prod

    #right diagonals
    for r in range(0,17):
        for c in range(0,17):
            prod = grid[r][c]*grid[r+1][c+1]*grid[r+2][c+2]*grid[r+3][c+3]
            if(prod>biggest): biggest=prod

    return biggest
    

'''See https://pythonandr.com/2015/09/01/highly-divisible-triangular-number-project-euler-problem-12/
for the i+11168 rather than i
it has to do with the triangle number closest
to the smallest number with 500 divisors'''
def Euler12():
    i=1
    while(True):
        nthTri = (i+11168)*(i+11169)//2
        divisors=0
        for j in range(1,int(nthTri**.5)+1,1):
            if(nthTri%j==0): divisors+=2
        if(divisors>500): return nthTri
        i+=1


def Euler13():
    digits = [37107287533902102798797998220837590246510135740250,
46376937677490009712648124896970078050417018260538,
74324986199524741059474233309513058123726617309629,
91942213363574161572522430563301811072406154908250,
23067588207539346171171980310421047513778063246676,
89261670696623633820136378418383684178734361726757,
28112879812849979408065481931592621691275889832738,
44274228917432520321923589422876796487670272189318,
47451445736001306439091167216856844588711603153276,
70386486105843025439939619828917593665686757934951,
62176457141856560629502157223196586755079324193331,
64906352462741904929101432445813822663347944758178,
92575867718337217661963751590579239728245598838407,
58203565325359399008402633568948830189458628227828,
80181199384826282014278194139940567587151170094390,
35398664372827112653829987240784473053190104293586,
86515506006295864861532075273371959191420517255829,
71693888707715466499115593487603532921714970056938,
54370070576826684624621495650076471787294438377604,
53282654108756828443191190634694037855217779295145,
36123272525000296071075082563815656710885258350721,
45876576172410976447339110607218265236877223636045,
17423706905851860660448207621209813287860733969412,
81142660418086830619328460811191061556940512689692,
51934325451728388641918047049293215058642563049483,
62467221648435076201727918039944693004732956340691,
15732444386908125794514089057706229429197107928209,
55037687525678773091862540744969844508330393682126,
18336384825330154686196124348767681297534375946515,
80386287592878490201521685554828717201219257766954,
78182833757993103614740356856449095527097864797581,
16726320100436897842553539920931837441497806860984,
48403098129077791799088218795327364475675590848030,
87086987551392711854517078544161852424320693150332,
59959406895756536782107074926966537676326235447210,
69793950679652694742597709739166693763042633987085,
41052684708299085211399427365734116182760315001271,
65378607361501080857009149939512557028198746004375,
35829035317434717326932123578154982629742552737307,
94953759765105305946966067683156574377167401875275,
88902802571733229619176668713819931811048770190271,
25267680276078003013678680992525463401061632866526,
36270218540497705585629946580636237993140746255962,
24074486908231174977792365466257246923322810917141,
91430288197103288597806669760892938638285025333403,
34413065578016127815921815005561868836468420090470,
23053081172816430487623791969842487255036638784583,
11487696932154902810424020138335124462181441773470,
63783299490636259666498587618221225225512486764533,
67720186971698544312419572409913959008952310058822,
95548255300263520781532296796249481641953868218774,
76085327132285723110424803456124867697064507995236,
37774242535411291684276865538926205024910326572967,
23701913275725675285653248258265463092207058596522,
29798860272258331913126375147341994889534765745501,
18495701454879288984856827726077713721403798879715,
38298203783031473527721580348144513491373226651381,
34829543829199918180278916522431027392251122869539,
40957953066405232632538044100059654939159879593635,
29746152185502371307642255121183693803580388584903,
41698116222072977186158236678424689157993532961922,
62467957194401269043877107275048102390895523597457,
23189706772547915061505504953922979530901129967519,
86188088225875314529584099251203829009407770775672,
11306739708304724483816533873502340845647058077308,
82959174767140363198008187129011875491310547126581,
97623331044818386269515456334926366572897563400500,
42846280183517070527831839425882145521227251250327,
55121603546981200581762165212827652751691296897789,
32238195734329339946437501907836945765883352399886,
75506164965184775180738168837861091527357929701337,
62177842752192623401942399639168044983993173312731,
32924185707147349566916674687634660915035914677504,
99518671430235219628894890102423325116913619626622,
73267460800591547471830798392868535206946944540724,
76841822524674417161514036427982273348055556214818,
97142617910342598647204516893989422179826088076852,
87783646182799346313767754307809363333018982642090,
10848802521674670883215120185883543223812876952786,
71329612474782464538636993009049310363619763878039,
62184073572399794223406235393808339651327408011116,
66627891981488087797941876876144230030984490851411,
60661826293682836764744779239180335110989069790714,
85786944089552990653640447425576083659976645795096,
66024396409905389607120198219976047599490197230297,
64913982680032973156037120041377903785566085089252,
16730939319872750275468906903707539413042652315011,
94809377245048795150954100921645863754710598436791,
78639167021187492431995700641917969777599028300699,
15368713711936614952811305876380278410754449733078,
40789923115535562561142322423255033685442488917353,
44889911501440648020369068063960672322193204149535,
41503128880339536053299340368006977710650566631954,
81234880673210146739058568557934581403627822703280,
82616570773948327592232845941706525094512325230608,
22918802058777319719839450180888072429661980811197,
77158542502016545090413245809786882778948721859617,
72107838435069186155435662884062257473692284509516,
20849603980134001723930671666823555245252804609722,
53503534226472524250874054075591789781264330331690]

    return str(sum(digits))[:10]


def Euler14(n):
    
    biggest=1
    out=1
    for n in range(1,n):
        inp = n        
        steps = 0
        while inp>1:
            if(inp%2==0): inp=inp/2
            else: inp = (3*inp)+1
            steps+=1
        if(steps>biggest):
            biggest=steps
            out=n
    return out


def Euler15(n):
    '''
    good=0
    for i in range(2**(n-1),2**(2*n-1)-2**(n-2)):
        out=""
        ones=0
        a=i
        while(a>=1):
            out+=str(a%2)
            if(str(a%2)=="1"): ones+=1
            a=int((a-a%2)/2)
        out = out[::-1]
        if(ones==n): good+=1
    return 2*good
    '''
    #The above code works (super slow) but...
    #According to the OEIS A000984, the following will always be (2n)!/(n!)^2
    #This is correct because the binary sequence has 2n slots with n 1's and n 0's
    #So, the expression is C(2n,n)=(2n)!/(n!)^2
    return math.factorial(2*n)//math.factorial(n)**2
    

def Euler16(n): return sum(int(digit) for digit in str(2**n)) #One Liner!


def Euler17(n):
    nums = ["one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["twenty","thrity","forty","fifty","sixty","seventy","eighty","ninety"]
    hundred = ["hundred"]
    thousand = ["thousand"]

    tLen=3 #"One" is already included
    for h in range(2,n+1):
        num=h
        strNum=str(h)
        for i in range(0,len(strNum)):
            if(i==3): tLen+=len(nums[int(strNum[:1])-1]+thousand[0])
            
            elif(i==2): #Hundreds
                if(strNum[len(strNum)-3]!="0"): tLen+=len(nums[int(strNum[len(strNum)-3])-1]+hundred[0])
                    
            elif(i==1): #Tens
                if(strNum[len(strNum)-2]!="0"):
                    if(strNum[len(strNum)-2]=="1"): tLen+=len(teens[int(strNum[len(strNum)-1])]) #Teens
                    else: tLen+=len(tens[int(strNum[len(strNum)-2])-2])
                if(len(strNum)>=3 and strNum[-2:]!="00"): tLen+=len("and") #ex. "one hundred and one" but not "and ninety nine"
                        
            elif((i==0 and strNum[len(strNum)-2]!="1")): #Ones that aren't part of teens
                if(strNum[len(strNum)-1]!="0"): tLen+=len(nums[int(strNum[len(strNum)-1])-1])
    return tLen

def Euler18():
    triangle = [[75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

    i=-2
    upperRow, lowerRow = triangle[i], triangle[-1]
    while(len(upperRow)>1):
        newLower=[] #New lower Row
        for i in range(0,len(upperRow)): newLower.append(upperRow[i]+max(lowerRow[i],lowerRow[i+1]))
        lowerRow = newLower
        i-=1
        upperRow = triangle[i]

    maxLen = upperRow[0]+max(lowerRow[0],lowerRow[1])
    return maxLen    
    
def Euler19():
    sundays=0
    for y in range(1910,2001):
        for m in range(1,13):
            d = 1
            
            isLY=False
            if(y%4==0):
                isLY=True
                if(y%100==0):
                    isLY=False
                    if(y%400==0): isLY=True
                        
            monthCodes = [6,2,2,5,0,3,5,1,4,6,2,4]
            monthCode = monthCodes[m-1]
            if((m==1 or m==2) and isLY==True): monthCode-=1

            dayCode = d

            cent = int(y/100)%4
            abbYr = y%100
            preYr=0
            if(abbYr in [0,6,17,23,28,34,45,51,56,62,73,79,84,90]): preYr=0
            if(abbYr in[1,7,12,18,29,35,40,46,57,63,68,74,85,91,96]): preYr=1
            if(abbYr in[2,13,19,24,30,41,47,52,58,69,75,80,86,97]): apreYr=2
            if(abbYr in[3,8,14,25,31,36,42,53,59,64,70,81,87,92,98]): preYr=3
            if(abbYr in[9,15,20,26,37,43,48,54,65,71,76,82,93,99]): preYr=4
            if(abbYr in[4,10,21,27,32,38,49,55,60,66,77,83,88,94]): preYr=5
            if(abbYr in[5,11,16,22,33,39,44,50,61,67,72,78,89,95]): preYr=6
            preYr+=int((7/6)*(cent)**3 + (-7)*(cent)**2 + (65/6)*(cent))
            yearCode = preYr%7
            
            day=(dayCode+monthCode+yearCode)%7
            if(day==0): sundays+=1
    return sundays


def Euler20(n): return sum(int(digit) for digit in str(math.factorial(n))) #One Line again

    
def Euler21(n):
    amicsSum=0
    for i in range(1,n):
        x=d(i)
        if(x!=i and i<x and d(x)==i): #If sum of sum of divisors of a number is that number w/ no double counting...
            amicsSum+=(x+i)
    return amicsSum


def Euler22():
    with open("names.txt") as f: names = f.read().split(',')
    names.sort()
    return sum((names.index(name)+1)*sum(string.ascii_uppercase.index(char)+1 for char in name.strip('"')) for name in names)


def Euler23():
    abund=[]
    for i in range(2,28124):
        if(d(i)>i): abund.append(i)
    possibles=set()
    for j in range(0,len(abund)):
        for k in range(j,len(abund)):
            s=abund[j]+abund[k]
            if(s<=28123): possibles.add(s) #All numbers >28123 can be written as the sum of abundants
    out=0
    for m in range(1,28124):
        if(m not in possibles): out+=m
    return out


from itertools import permutations #How to do this myself?
def Euler24(n): return ''.join(list(permutations('0123456789'))[n-1]) #Another one liner!


def Euler25(n):
    a=1
    b=1 #index 2
    i=2
    while(len(str(b))<n):
        a,b = b,a+b
        i+=1
    return i


def Euler26(n):
    biggest=1 #certain primes p will have cycles of p-1, so we want to look for them  
    out=1
    for i in range(n-1,n//2 +1,-1): #searching in reverse, always a prime between n and 2n
        if(i%2!=0 and i%3!=0 and i%5!=0 and ((i-1)%6==0 or (i+1)%6==0) and i%7!=0 and i%11!=0 and i%13!=0 and i%17!=0 and i%19!=0 and i%23!=0 and i%29!=0): #check for small primes
            for j in range(1,i): #Will find period for all repeating decimals
                if((10**j -1)%i==0):
                    if(j>biggest):
                        biggest=j
                        out=i
                    break
            if(i-1==biggest): break
    return out


def Euler27():
    biggest,i,coeffs=0,0,[0,0]
    for a in range(-999,1000):
        for b in range(-1000,1001):
            n=0
            if(b>a): #Since all primes are pos, b must > a for Quad(a,b,0)>0
                while(isPrime(Quad(a,b,n))==True):
                    n+=1
                    if(n>biggest): biggest, coeffs = n, [a,b]
    return coeffs[0]*coeffs[1]


def Euler28(n):
    prev, out=1,1 #1x1 case is clearly 1
    for i in range(3,n+1,2):
        out=prev+ 4*(i**2) -6*(i-1) #The next odd one is the previious plus the outer corners
        prev=out
    return out


def Euler29(n):
    ab = set()
    for a in range(2,n+1):
        for b in range(2,n+1):
            ab.add(a**b)
    return len(ab)
    

def Euler30():
    out=0
    for i in range(10,295246): #295245 = 5* 9^5 -->Max possible value
        if(Digit5th(str(i))==True):
            out+=i
            print(i)
    return out
    

def Euler31(n): #umber of ways to make n pence with British coins
    target, ways = n, 0
    #We will find all ways, padding w/ 1p coins when needed
    for a in range(target,-1,-200): #200p
        for b in range(a,-1,-100): #100p
            for c in range(b,-1,-50): #50p
                for d in range(c,-1,-20): #20p
                    for e in range(d,-1,-10): #10p
                        for f in range(e,-1,-5): #5p
                            for g in range(f,-1,-2): #2p
                                ways+=1 #1p is considered to be padded when needed
    return ways


def Euler32():
    total=0
    for i in range(1000,int(math.sqrt(987654321)+1)):
        for j in range(1,int(math.sqrt(i)+1)):
            if(i%j==0):
                s = str(i)+str(j)+str(i//j)
                if(isPandigital(s,9)==True):
                    total+=i
                    break
    return total


def Euler33():
    prod, denom = 1, 1 #product of fractions, counter
    for fdn in range(1,10): #Always [1,9] b/c end zeroes are trivial, and leading zeroes make no sense (01=1)
        for sdn in range(1,10):
            for fdd in range(1,10):
                for sdd in range(1,10):
                    if(10*fdn+sdn < 10*fdd+sdd): #Less than 1
                        #one digit in numerator/denominator must be same, but not both
                        if(fdn==fdd and (10*fdn+sdn)/(10*fdd+sdd) == sdn/sdd): prod*=sdn/sdd
                        elif(fdn==sdd and (10*fdn+sdn)/(10*fdd+sdd) == sdn/fdd): prod*=sdn/fdd 
                        elif(sdn==fdd and (10*fdn+sdn)/(10*fdd+sdd) == fdn/sdd): prod*=fdn/sdd 
                        elif(sdn==sdd and (10*fdn+sdn)/(10*fdd+sdd) == sdn/fdd): prod*=snd/fdd 
                        
    while(abs(int(denom*prod) - denom*prod) > 10**-15): denom+=1 #no float point probs (16 place prec.)
    return denom


def Euler34():
    out=0
    for i in range(3,362881): #9! was a upper bound guess that happened to be OK
        if("9" not in str(i) and isFactorialSum(i)): out+=i #having a 9 seems too big to be an acceptable sum
    return out


def Euler35():
    count = 4 #2,3,5,7 are already included
    for i in range(11,1000000,2): #next prime is 11
        if("5" not in str(i) and i%3!=0): addToCount=True
        else: addToCount=False
        if(addToCount==True):
            perms = Rotate(i)
            for num in perms:
                if(isPrime(num)==False):
                    addToCount=False
                    break
                
            if(addToCount==True): count+=1
    return count


def Euler36():
    count=0
    for i in range(1,1000000):
        if(isPalindronic(str(i)) and isPalindronic(decToBin(i))): count+=i
    return count

    
def Euler37():
    primeCount, total, i = 0, 0, 11
    while(primeCount<11):
        addCount=True
        trunc = Trunc(str(i))
        for num in trunc:
            if(isPrime(num)==False):
                addCount=False
                break
        if(addCount==True):
            primeCount+=1
            total+=i
        i+=1
    return total 


def Euler38():
    biggest=1
    for a in range(1,10000):
        strNum = ""
        for n in range(1,10): 
            strNum+=str(a*n)
            if(len(strNum)==9 and isPandigital(strNum,9) and int(strNum)>biggest): biggest=int(strNum)
    return biggest


def Euler39(n):
    biggest, out = 1, 1
    for perim in range(3,n+1):
        sols=0
        for a in range(1,perim//2 +1):
            for b in range(1,a+1):
                if(math.sqrt(a**2 + b**2)+a+b==perim): sols+=1
        if(sols>biggest): biggest, out = sols, 
    return out


def Euler40():
    champ=""
    for i in range(1,200000): champ+=str(i)
    return int(champ[1-1])*int(champ[10-1])*int(champ[100-1])*int(champ[1000-1])*int(champ[10000-1])*int(champ[100000-1])*int(champ[1000000-1])


def Euler41():
    numS, biggest, nums = list(permutations('1234567')), 1, [] #8, 9 digit pandigitals all divide 3 -- biggest prob 7 digit
    for s in numS: nums.append(int(''.join(s)))
    nums.sort(reverse=True)
    for n in nums:
        if(isPrime(n)): return n


def Euler42():
    with open("words.txt") as f: words = f.read().split(',') #put common words into list    #words.sort()
    return sum(isTriS(word.strip('"')) for word in words)


def Euler43():
    numS, total, nums, smallPrimes = list(permutations('0123456789')), 0, [], [2,3,5,7,11,13,17]
    for s in numS: nums.append(int(''.join(s)))
    for p in nums:
        strP, addNum = [str(p)[1:4], str(p)[2:5], str(p)[3:6], str(p)[4:7], str(p)[5:8], str(p)[6:9], str(p)[7:]], True
        for i in range(len(strP)):
            if(int(strP[i])%smallPrimes[i]!=0):
                addNum=False
                break
        if(addNum==True): total+=p
    return total


def Euler44():
    pents, smallest = [], 0
    for i in range(1,2200): pents.append(i*(3*i-1)//2)    
    for j in range(len(pents)):
        for k in range(j):
            s=pents[k]+pents[j]
            d=abs(pents[k]-pents[j])
            if(isPent(s) and isPent(d)): smallest=d
    return smallest


def Euler45():
    for i in range(10000,100000):
        hexa = i*(2*i-1)
        if(isPent(hexa)): return hexa


def Euler46():
    for i in range(5,10000,6): #Find smallest odd comp. number that can't be written as sum of prime and twice a square
        fail=True #does a number fail the conj.
        if(i%2==1 and (i+1)%6==0 and isPrime(i)==False):
            for p in range(3,i-5,2):
                if(isPrime(p)):
                    for s in range(2,int(math.sqrt((i-p)/2)+1)):
                        if(i==p+ 2*(s**2)):
                            fail=False
                            break
                    if(fail==False): break
                if(fail==False): break
            if(fail==True): return i
    print("ERROR")


def Euler47(): #how to imporve for large number inputs
    i =  210 #2*3*5*7
    f2 = Factor(i)[-1]
    s2 = Factor(i+1)[-1]
    t2 = Factor(i+2)[-1]
    while(True):
        fo2 = Factor(i+3)[-1]
        if(i%100==0):print(i)
        if((f2<4 or s2<4 or t2<4 or fo2<4)==False): return i
        f2 = s2 #only hae to call Factor() once per loop
        s2 = t2
        t2 = fo2
        i+=1


def Euler48(n): return str(sum((i**i)%(10**10) for i in range(1,n+1)))[-10:]


def Euler49():
    for i in range(100001,1000000,2):
        if(isPrime(i)):
            for add in range(2,int((1000000-i)/2)+1,2):
                if(i+2*add < 1000000):
                    a=i+add
                    if(sorted(str(i))==sorted(str(a)) and isPrime(a)):
                        b=a+add
                        if(sorted(str(i))==sorted(str(b)) and isPrime(b)):
                            print("%i,%i,%i -- %i"%(i,a,b,add))


def Euler50():
    primes,maxPrime,i=[2],2,3 #2 is included
    while(maxPrime<10000): #is primes up to 10,000 enough?
        if(isPrime(i)):
            primes.append(i)
            maxPrime=i
        i+=2

    L,best=1,0 #length of chain
    while(L<600): #max chain length=600 (enough?)
        for j in range(0,L):
            total=0
            for k in range(0,L):
                total+=primes[k+j]
                if(total>1000000): break
            if(total>1000000): break
            elif(100000<total<1000000 and isPrime(total)): best=total
        L+=1
    return best


def Euler51(): print("To Do")
##########################  IN PROGRESS -- HARD  ####################
'''
** Will have 5 or 6 digits -- >=3 replaced
** No replaced digit at end of number (0,2,4,5,6,8) won't work
** No replaced digit or 0 at beginning of number
** Failed replacements must make num divisible by 3 or 11
** If replacing 3 digits, first and last digits CANNOT add to multiple of 3

CHECKED
** If number is 5 digits and replacing 3, it doesn't end in 1
** If number is 5 digits and replacing 3, it doesn't end in 3
** If number is 5 digits and replacing 3, it doesn't end in 7
** If number is 5 digits and replacing 3, it doesn't end in 9
THEREFORE
** Will have 6 digits -- >=3 replaced

*'s could possibly be replaced
** Number: (#1-9)****(1,3,7,9)

** If a repeating digit is first, all repeatings must be [1-9]
'''
    

def Euler52():
    for i in range(100000,1000000):
        if(sorted(str(i))==sorted(str(2*i))==sorted(str(3*i))==sorted(str(4*i))==sorted(str(5*i))==sorted(str(6*i))): return i


def Euler53():
    total=0
    for n in range(1,101):
        for r in range(0,n+1):
            if(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)) > 1000000):
                total+=1
    return total


def Euler54(): print("To Do")


def Euler55():
    lynchTotal=0
    for num in range(1,100000):
        isLynch=True
        check=num
        for i in range(0,1000):
            check+=Reverse(check)
            if(isPalindronic(str(check))):
                isLynch=False
                break
        if(isLynch):
            lynchTotal+=1
            with open("b023108.txt","a") as f:
                f.write(str(lynchTotal)+" "+str(num)+"\n")
            print(lynchTotal,num)
    return lynchTotal


def Euler56():
    biggest=1
    for a in range(90,100): #prob in 90^90 -- 99^99 range
        for b in range(90,100):
            s = digitSum(str(a**b))
            if(s>biggest): biggest = s
    return biggest


def Euler57():
    total=0
    frac = [3,2]
    for p in range(1,1001):
        if( len(str(frac[0])) > len(str(frac[1])) ): total+=1
        frac = nextApproxRoot2(frac[0],frac[1])
    return total


def Euler58(): #must be odd
    lDiag=5
    totalPrimes=3 #3,5,7
    i=5
    while(totalPrimes/lDiag>.1):
        Pcorners = [i**2 - 3*(i-1),i**2 - 2*(i-1),i**2 - (i-1)]
        lDiag+=4
        for p in Pcorners:
            if(isPrime(p)): totalPrimes+=1
        i+=2
    return i-2


def Euler59():
    cipherSmall = [79,59,12,2,79,35,8,28,20,2,3,68,8,9,68,45,0,12,9,67,68,4,7,5,23,27,1,21,79,85,78,79,85,71,38,10,71,27,12,2,79,6,2,8,13,9,1,13,9,8,68,19,7,1,71,56,11,21,11,68,6,3,22,2,14,0,30,79,1,31,6,23,19,10,0,73,79,44,2,79,19,6,28,68,16,6,16,15,79,35,8,11,72,71,14,10,3,79,12,2,79,19,6,28,68,32,0,0,73,79,86,71,39,1,71,24,5,20,79,13,9,79,16,15,10,68,5,10,3,14,1,10,14,1,3,71,24,13,19,7,68,32,0,0,73,79,87,71,39,1,71,12,22,2,14,16,2,11,68,2,25,1,21,22,16,15,6,10,0,79,16,15,10,22,2,79,13,20,65,68,41,0,16,15,6,10,0,79,1,31,6,23,19,28,68,19,7,5,19,79,12,2,79,0,14,11,10,64,27,68,10,14,15,2,65,68,83,79,40,14,9,1,71,6,16,20,10,8,1,79,19,6,28,68,14,1,68,15,6,9,75,79,5,9,11,68,19,7,13,20,79,8,14,9,1,71,8,13,17,10,23,71,3,13,0,7,16,71,27,11,71,10,18,2,29,29,8,1,1,73,79,81,71,59,12,2,79,8,14,8,12,19,79,23,15,6,10,2,28,68,19,7,22,8,26,3,15,79,16,15,10,68,3,14,22,12,1,1,20,28,72,71,14,10,3,79,16,15,10,68,3,14,22,12,1,1,20,28,68,4,14,10,71,1,1,17,10,22,71,10,28,19,6,10,0,26,13,20,7,68,14,27,74,71,89,68,32,0,0,71,28,1,9,27,68,45,0,12,9,79,16,15,10,68,37,14,20,19,6,23,19,79,83,71,27,11,71,27,1,11,3,68,2,25,1,21,22,11,9,10,68,6,13,11,18,27,68,19,7,1,71,3,13,0,7,16,71,28,11,71,27,12,6,27,68,2,25,1,21,22,11,9,10,68,10,6,3,15,27,68,5,10,8,14,10,18,2,79,6,2,12,5,18,28,1,71,0,2,71,7,13,20,79,16,2,28,16,14,2,11,9,22,74,71,87,68,45,0,12,9,79,12,14,2,23,2,3,2,71,24,5,20,79,10,8,27,68,19,7,1,71,3,13,0,7,16,92,79,12,2,79,19,6,28,68,8,1,8,30,79,5,71,24,13,19,1,1,20,28,68,19,0,68,19,7,1,71,3,13,0,7,16,73,79,93,71,59,12,2,79,11,9,10,68,16,7,11,71,6,23,71,27,12,2,79,16,21,26,1,71,3,13,0,7,16,75,79,19,15,0,68,0,6,18,2,28,68,11,6,3,15,27,68,19,0,68,2,25,1,21,22,11,9,10,72,71,24,5,20,79,3,8,6,10,0,79,16,8,79,7,8,2,1,71,6,10,19,0,68,19,7,1,71,24,11,21,3,0,73,79,85,87,79,38,18,27,68,6,3,16,15,0,17,0,7,68,19,7,1,71,24,11,21,3,0,71,24,5,20,79,9,6,11,1,71,27,12,21,0,17,0,7,68,15,6,9,75,79,16,15,10,68,16,0,22,11,11,68,3,6,0,9,72,16,71,29,1,4,0,3,9,6,30,2,79,12,14,2,68,16,7,1,9,79,12,2,79,7,6,2,1,73,79,85,86,79,33,17,10,10,71,6,10,71,7,13,20,79,11,16,1,68,11,14,10,3,79,5,9,11,68,6,2,11,9,8,68,15,6,23,71,0,19,9,79,20,2,0,20,11,10,72,71,7,1,71,24,5,20,79,10,8,27,68,6,12,7,2,31,16,2,11,74,71,94,86,71,45,17,19,79,16,8,79,5,11,3,68,16,7,11,71,13,1,11,6,1,17,10,0,71,7,13,10,79,5,9,11,68,6,12,7,2,31,16,2,11,68,15,6,9,75,79,12,2,79,3,6,25,1,71,27,12,2,79,22,14,8,12,19,79,16,8,79,6,2,12,11,10,10,68,4,7,13,11,11,22,2,1,68,8,9,68,32,0,0,73,79,85,84,79,48,15,10,29,71,14,22,2,79,22,2,13,11,21,1,69,71,59,12,14,28,68,14,28,68,9,0,16,71,14,68,23,7,29,20,6,7,6,3,68,5,6,22,19,7,68,21,10,23,18,3,16,14,1,3,71,9,22,8,2,68,15,26,9,6,1,68,23,14,23,20,6,11,9,79,11,21,79,20,11,14,10,75,79,16,15,6,23,71,29,1,5,6,22,19,7,68,4,0,9,2,28,68,1,29,11,10,79,35,8,11,74,86,91,68,52,0,68,19,7,1,71,56,11,21,11,68,5,10,7,6,2,1,71,7,17,10,14,10,71,14,10,3,79,8,14,25,1,3,79,12,2,29,1,71,0,10,71,10,5,21,27,12,71,14,9,8,1,3,71,26,23,73,79,44,2,79,19,6,28,68,1,26,8,11,79,11,1,79,17,9,9,5,14,3,13,9,8,68,11,0,18,2,79,5,9,11,68,1,14,13,19,7,2,18,3,10,2,28,23,73,79,37,9,11,68,16,10,68,15,14,18,2,79,23,2,10,10,71,7,13,20,79,3,11,0,22,30,67,68,19,7,1,71,8,8,8,29,29,71,0,2,71,27,12,2,79,11,9,3,29,71,60,11,9,79,11,1,79,16,15,10,68,33,14,16,15,10,22,73]
    for key1 in range(97,123):
        for key2 in range(97,123):
            for key3 in range(97,123):
                key = [key1,key2,key3]
                keyS = ASCIItoStr(key)
                s=ASCIItoStr(XOR(cipherSmall,key))
                if(hasAll(s)): print(" Key: "+keyS+"  Sum:",sum(XOR(cipherSmall,key)))
    return sum(XOR(cipherSmall,key))


# TO DO: 60, 61


def Euler62():
    cubes = []
    i=0
    while(True):
        cube = sorted(list(str(i**3))) #Sorts digits of a number cube
        cubes.append(cube) #appends digits as one element to a list
        if cubes.count(cube)==5: #if these digits are present five times...
            return cubes.index(cube)**3 #Return the cube's index in the list, cubed
        i+=1
        
############## To DO: 63 ################

 
def Euler64():
    total=0
    for i in range(1,10001):
        if(not isInteger(math.sqrt(i)) and getPeriod(i)%2==1): total+=1
    return total


def Euler65():
    numerator=[2,3]
    n=2
    for i in range(3,101):
        if(i%3==0):
            numerator = [numerator[1],n*numerator[1]+numerator[0]]
            n+=2
        else: numerator = [numerator[1],numerator[1]+numerator[0]]
    return digitSum(str(numerator[1]))


'''
Square root continued fractions can have eight odd or even period.
Odd Periods: Solution to Pell Equation at 2*period(th) convergent
Even Periods: Solution to Pell Equation at period(th) convergent
'''
               
def Euler66():
    maxIX = [0,0]
    for i in range(1,1001):
        if(isInteger(math.sqrt(i))==False):
            XY = MinPell(i)
            if(XY[0]>maxIX[1]): maxIX = [i,XY[0]]
    return maxIX[0]


def Euler67():
    triangle = getTriangle("tri_big.txt")
    i=-2
    upperRow, lowerRow = triangle[i], triangle[-1]
    while(len(upperRow)>1):
        newLower=[] #New lower Row
        for i in range(0,len(upperRow)): newLower.append(upperRow[i]+max(lowerRow[i],lowerRow[i+1]))
        lowerRow = newLower
        i-=1
        upperRow = triangle[i]
        
    maxLen = upperRow[0]+max(lowerRow[0],lowerRow[1])
    return maxLen


def Euler68(): print("To Do")


def Euler69(n):
    primorial,i,primes=1,0,[2]
    for j in range(3,int(math.sqrt(n/math.log(n))),2):
        if(isPrime(j)): primes.append(j)
    while(primorial*primes[i]<n):
        primorial*=primes[i]
        i+=1
    return primorials


#####################
#    TO DO 70-91    #
#####################
    
def Euler92():
    count=0
    for i in range(2,10000000):
        if isSmallestComb(i):
            chain = squareChain(i)
            if(89 in chain):
                count+=digitMultinomial(i)
    return count


# TO DO: 93-96


def Euler97():
    # Used CRT and Euler's Theorem to find that the last 10 digits of 2^7830457 must be the smallest number to satisfy
    # C = 0(0 mod 2^10)
    # C = 3038247 (mod 5^10) -- 3038247 = 2^17947(mod 5^10); 17947 = 7830457 (mod phi(5^10)))
    # Which is equivalent to wanting to find
    # C = a*5^10 + 3038247 = b*2^10
    x, y, a = 5**10, 3038247, 0
    while((a*x+y)%(2**10)!=0): a+=1
    C = a*x + y
    return int(str(C*28433 + 1)[-10:])

    #Note that ((28433*(2**7830457))+1)%(10**10) will also quickly give the answer. This isn't as cool though


#TO DO: 98, 99


'''
The first few solutions for blues are:
3,
15,
85,
493,
2871,
from OEIS:
b(n) = 6*b(n-1) - b(n-1) - 2, b(0)=1, b(1)=3

The first few solutions for reds are:
1,
6,
35,
204,
1189,
from OEIS
r(n) = 6*r(n-1) - r(n-1), r(0)=0, r(1)=1
'''
def Euler100(target):
    bluePrev2, redPrev2 = 3, 1
    bluePrev, redPrev = 15, 6
    blue, red = 6*bluePrev - bluePrev2 -2, 6*redPrev - redPrev2
    total = blue+red

    while(total<=target):
        bluePrev2, redPrev2 = bluePrev, redPrev
        bluePrev, redPrev = blue, red
        blue, red = 6*bluePrev - bluePrev2 -2, 6*redPrev - redPrev2
        total=blue+red
        
    return blue
