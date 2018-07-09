'''
This finds the minimal number of clicks needed to solve any 5x5 board. 
I had previously found that it is either 15, 16, or 17 clicks.
This program checks all boards created (and solveable) in 16 and 17 clicks.
'''

def boardModAdd(m,a):
    out=""
    for i in range(25):
        if m[i]==a[i]: out+="0"
        else: out+="1"
    return out


def main():
    sixteenBoards, seventeenBoards = [], []
    #First 16 board is '0000000001111111111111111' = 65535
    #Last  17 board is '1111111111111111100000000' = 33554176
    for i in range(65535,33554176+1):
        b = ("{0:b}".format(i)).zfill(25)
        if b.count("1")==16: sixteenBoards.append(b)
        elif b.count("1")==17: seventeenBoards.append(b)
        
    print("All boards generated")

    #Null boards
    N1 = "1010110101000001010110101"
    N2 = "1101100000110110000011011"
    N3 = "0111010101110111010101110"

    #Check 16-click boards
    for board in sixteenBoards:
        S1 = boardModAdd(board,N1).count("1")
        S2 = boardModAdd(board,N2).count("1")
        S3 = boardModAdd(board,N3).count("1")
        if S1>15 and S2>15 and S3>15: print(board)
    print("All 16-click boards checked")

    #Check 17-click boards
    for board in seventeenBoards:
        S1 = boardModAdd(board,N1).count("1")
        S2 = boardModAdd(board,N2).count("1")
        S3 = boardModAdd(board,N3).count("1")
        if S1>15 and S2>15 and S3>15: print(board)
    print("All 17-click boards checked")



