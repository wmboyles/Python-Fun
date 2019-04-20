def oddZeroRuns(s):
    oddRuns = 0
    runLen = 0
    for char in s:
        if char == "0": runLen += 1
        else:
            if(runLen > 0 and runLen % 2 == 1):
                oddRuns += 1
                runLen = 0

    if(runLen > 0 and runLen % 2 == 1): oddRuns += 1
    
    return oddRuns


def main(n):
    out = ""
    for i in range(n + 1):
        if(oddZeroRuns(bin(i)[2:]) == 0 or i == 0): out += "1"
        else: out += "0"

    return out
