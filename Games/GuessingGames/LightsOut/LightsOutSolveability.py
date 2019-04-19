import numpy as np

#IDEA: Have a 5x5 GUI that allows the user to click color-changing buttons in order to set the board

def main():
    N1 = np.array([[0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0]]) #The board must be orthagonal to these two vectors mod 2 in order to be solveable
    N2 = np.array([[1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1]])

    Board = np.zeros((25,1), dtype=int) #make board (column vector)
    DispBoard = Board.reshape((5,5)) #reshape board for display
    for i in range(0,5): #get board state from user
        for j in range(0,5):
            DispBoard[i,j]=int(input("(%i,%i): "%(i+1,j+1)))%2

    print('\n'.join(' '.join(str(cell) for cell in row) for row in DispBoard)) #format board for display
    
    if (int(np.dot(N1,Board))%2==0 and int(np.dot(N2,Board))%2==0): #return solveability verdict
        print("The board is solveable")
    else:
        print("The board is unsolveable")

    Again = input("Again (Y/N): ") #Run again?
    if(Again=='Y' or Again=='y'):
        print('\n'+'\n'+'\n')
        main()
    else:
        return 0

main()
