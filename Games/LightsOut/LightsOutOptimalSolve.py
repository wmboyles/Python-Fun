import numpy as np
from random import randint

StateBoard = np.zeros((5, 5), dtype=int)  # Make a blank 5x5 board (Null State). This will be the state of play
OperationBoard = np.zeros((5, 5), dtype=int)  # This will be the board that records what was clicked
'''
The board runs from 0 to 4 in both directions. X is the horizontal (first number)
Y is the vertical (second number). The top left is (0,0). The bottom right is (4,4)
'''


def Click(x, y):  # Function changes the state of lights (x,y) and adjacent lights
    # Changes the state of selected light. NumPy lists the Y cordinate first.
    if StateBoard[y, x] == 0: StateBoard[y, x] = 1
    else: StateBoard[y, x] = 0

    # To the left
    if x > 0:
        if StateBoard[y, x - 1] == 0: StateBoard[y, x - 1] = 1
        else: StateBoard[y, x - 1] = 0

    # To the right
    if x < 4:
        if StateBoard[y, x + 1] == 0: StateBoard[y, x + 1] = 1
        else: StateBoard[y, x + 1] = 0

    # Above
    if y > 0:
        if StateBoard[y - 1, x] == 0: StateBoard[y - 1, x] = 1
        else: StateBoard[y - 1, x] = 0

    # Below
    if y < 4:
        if StateBoard[y + 1, x] == 0: StateBoard[y + 1, x] = 1
        else: StateBoard[y + 1, x] = 0

    OperationBoard[y, x] = (OperationBoard[y, x] + 1) % 2


def LightChase():  # Carries out the LightChasing procedure  
    # Chases lights down to last row
    for y in range(4):
        for x in range(5):
            if StateBoard[y, x] == 1: Click(x, y + 1)

    if(StateBoard[4, 0] == 1 and StateBoard[4, 1] == 0 and StateBoard[4, 2] == 0 and StateBoard[4, 3] == 0 and StateBoard[4, 4] == 1):
        Click(0, 0)
        Click(1, 0)

    elif(StateBoard[4, 0] == 0 and StateBoard[4, 1] == 1 and StateBoard[4, 2] == 0 and StateBoard[4, 3] == 1 and StateBoard[4, 4] == 0):
        Click(0, 0)
        Click(3, 0)

    elif(StateBoard[4, 0] == 1 and StateBoard[4, 1] == 1 and StateBoard[4, 2] == 1 and StateBoard[4, 3] == 0 and StateBoard[4, 4] == 0): Click(1, 0)

    elif(StateBoard[4, 0] == 0 and StateBoard[4, 1] == 0 and StateBoard[4, 2] == 1 and StateBoard[4, 3] == 1 and StateBoard[4, 4] == 1): Click(3, 0)

    elif(StateBoard[4, 0] == 1 and StateBoard[4, 1] == 0 and StateBoard[4, 2] == 1 and StateBoard[4, 3] == 1 and StateBoard[4, 4] == 0): Click(4, 0)

    elif(StateBoard[4, 0] == 0 and StateBoard[4, 1] == 1 and StateBoard[4, 2] == 1 and StateBoard[4, 3] == 0 and StateBoard[4, 4] == 1): Click(0, 0)

    elif(StateBoard[4, 0] == 1 and StateBoard[4, 1] == 1 and StateBoard[4, 2] == 0 and StateBoard[4, 3] == 1 and StateBoard[4, 4] == 1): Click(2, 0)

    # Chases lights down to solved state
    for y in range(4):
        for x in range(5):
            if StateBoard[y, x] == 1: Click(x, y + 1)


def main():
    global StateBoard, OperationBoard
    StateBoard, OperationBoard = np.zeros((5, 5), dtype=int), np.zeros((5, 5), dtype=int)
    
    level = int(input("Level: ")) % 26
    while OperationBoard.sum() < level: Click(randint(0, 4), randint(0, 4))

    CreateBoard = OperationBoard  # A record of how the board was created
    print("CREATION BOARD")
    print(CreateBoard)
    print("-------------------------\nSTATE BOARD")
    print(StateBoard)

    OperationBoard = np.zeros((5, 5), dtype=int)  # Reset Operation board to zeroes

    LightChase()  # Solve board suboptimally

    Nulls = [np.array([[1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 1, 1]]), np.array([[1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1]]), np.array([[0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0]])]
    i = 0

    while i < 3:
        if(((OperationBoard - Nulls[i]) % 2).sum() < OperationBoard.sum()):
            OperationBoard = (OperationBoard - Nulls[i]) % 2
            i = 0
        else: i += 1

    print("-------------------------\nSOLVE BOARD -- %i clicks" % OperationBoard.sum())   
    print(OperationBoard)
    print("-------------------------\n")

    again = input("Again: ").lower()
    if again == "y" or again == "yes" or again == "1": main()


main()
'''
NOTE:
Neither The create board nor a level selection is needed to solve optimally.
These are just here so the user doesn't have to slowly enter a state board manually
'''
