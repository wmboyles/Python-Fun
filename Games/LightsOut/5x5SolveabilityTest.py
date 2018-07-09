import numpy as np

#IDEA: Have a 5x5 GUI that allows the user to click color-changing buttons in order to set the board


def solveable(board):
	#The board must be orthagonal to both of these two vectors modulo 2 in order to be solveable
    N1 = np.array([[0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0]])
    N2 = np.array([[1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1]])
    return (int(np.dot(N1,board))%2==0 and int(np.dot(N2,board))%2==0): #solveability verdict
   

def again():
	again = input("Again (Y/N): ")
	return again.lower() in 'y1'


def getStateBoard():
    stateBoard = np.zeros((5,5), dtype=int)
    for i in range(0,5): #get which lights are one from user
        for j in range(0,5):
            stateBoard[i,j]=int(input("(%i,%i): "%(i+1,j+1)))%2
			
	return state board
			
			
def main():
    board = np.zeros((25,1), dtype=int) #make empty board as column vector
    
    dispBoard = getStateBoard()
    
    if solveable(board): print("The board is solveable.")
    else: print("The board is not solveable.")

    if again(): main()

main()
