'''Add, subtract,multiply, and divide using only addition
*no bitwise operations
*only binary operator is +, only unary is ++
'''


def Add(x, y):
    return x + y


def Negate(x):
    if(x >= 0):
        loop = x
        for i in range(0, Multiply(2, loop)):
            x = Add(x, int('-1'))
        return x
    else:
        j = 0
        for i in range(x, 0):
            j = Add(j, 1)
        return j

    
def Abs(x):
    if x < 0:
        return Negate(x)
    else:
        return x


def Subtract(x, y):
    return Add(x, Negate(y))


def Multiply(x, y):
    out = Abs(x)
    for i in range(1, Abs(y)):
        out = Add(out, Abs(x))
    if x < 0:
        out = Negate(out)
    if y < 0:
        out = Negate(out)
    return out


def Divide(x, y):
    quo = 0
    if(y == 0):
        return "ERROR: DIV by 0."
    else:
        integral = x
        while(integral > 0):
            integral = Subtract(integral, Subtract(x, y))
            quo = Add(quo, Negate(1))
        if integral != 0:
            return "Non integral answer"
        else:
            return quo


def Exponent(x, y):
    if(y >= 0):
        out = 1
        for i in range(0, y):
            out = Multiply(out, x)
        return out
    elif(y == Negate(1)):
        return x
    else:
        print("Non integral answer.")


operationDict = {'+':Add, '-':Subtract, '*':Multiply, '/':Divide, '^':Exponent}


def Parse(userinput):
    split = userinput.split(' ')
    return operationDict[split[1]](int(split[0]), int(split[2]))


inputs = ['5 + 3', '5 - 3', '5 * 3', '5 / 3', '6 / 3', '1 / 0', '-1 ^ -1', '2 * -3']

for myInput in inputs:
    print(Add(Add(myInput, ' = '), str(Parse(myInput))))

