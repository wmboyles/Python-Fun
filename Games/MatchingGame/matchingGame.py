from random import randint

class Board: 
    def __init__(self,size):
        self.gameBoard, self.boardSize = [], size
        Board.makeRandBoard(self)

    def getSize(self): return self.boardSize

    def makeRandBoard(self): #Make a board of boardSize with random pairs of values in random positions
        value, cardValues = 0, list(range(0,(self.boardSize**2)//2))+list(range(0,(self.boardSize**2)//2))
        for i in range(self.boardSize): self.gameBoard.append([]) #Gives gameBoard proper number of rows
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                cardVal = randint(0,len(cardValues)-1)
                c1 = Card(cardValues[cardVal])
                self.gameBoard[i].append(c1)
                del cardValues[cardVal] #Delete specific index

    def matching(self,guesses): #Do the two cards in guesses match?
        pos1Row, pos1Col, pos2Row, pos2Col = guesses[0]//self.boardSize, guesses[0]%self.boardSize, guesses[1]//self.boardSize, guesses[1]%self.boardSize
        if self.gameBoard[pos1Row][pos1Col].getValue() == self.gameBoard[pos2Row][pos2Col].getValue(): return True
        else: return False
    
    def flipCards(self,guesses): #Flips all cards of gameBoard in guesses
        pos1Row, pos1Col, pos2Row, pos2Col = guesses[0]//self.boardSize, guesses[0]%self.boardSize, guesses[1]//self.boardSize, guesses[1]%self.boardSize
        self.gameBoard[pos1Row][pos1Col].flip()
        self.gameBoard[pos2Row][pos2Col].flip()

    def isSolved(self):
        for l in self.gameBoard:
            for card in l:
                if(card.isMatched == False): return False
        return True

    def printEntireBoard(self):
        for i in range(self.boardSize):
            out=""
            for j in range(self.boardSize):
                if j!=self.boardSize-1: out+=str(self.gameBoard[i][j].getValue())+", "
                else: out+=str(self.gameBoard[i][j].getValue())
            print(out)

    def printBoard(self):
        for i in range(self.boardSize):
            out=""
            for j in range(self.boardSize):
                if j!=self.boardSize-1: #Last line
                    if self.gameBoard[i][j].isMatched: out+=str(self.gameBoard[i][j].getValue())+", "
                    else: out+="?, "
                elif(self.gameBoard[i][j].isMatched): out+=str(self.gameBoard[i][j].getValue())
                else: out+="?"
            print(out)
  
    def printSpecBoard(self,guesses): #Print the board normally, but with all cards in guesses face-up
        pos1Row, pos1Col, pos2Row, pos2Col = guesses[0]//self.boardSize, guesses[0]%self.boardSize, guesses[1]//self.boardSize, guesses[1]%self.boardSize
        for i in range(self.boardSize):
            out=""
            for j in range(self.boardSize):
                if j!=self.boardSize-1:
                    if self.gameBoard[i][j].isMatched or (i==pos1Row and j==pos1Col) or (i==pos2Row and j==pos2Col): out+=str(self.gameBoard[i][j].getValue())+", "
                    else: out+="?, "
                elif self.gameBoard[i][j].isMatched or (i==pos1Row and j==pos1Col) or (i==pos2Row and j==pos2Col): out+=str(self.gameBoard[i][j].getValue())
                else: out+="?"
            print(out)

        
class GameRunner:
    def __init__(self):
        boardSize, self.numGuesses = self.getBoardSize(), 0
        numCards = boardSize**2
        
        gameBoard = Board(boardSize)      
        gameBoard.printBoard()

        guesses = [-1,-1]
        
        while(gameBoard.isSolved()==False):
            guesses = self.makeGuess()

            if(guesses[0]>numCards or guesses[0]<0 or guesses[1]>numCards or guesses[1]<0):
                print("Invalid position...\n")
                guesses = self.makeGuess();

            gameBoard.printSpecBoard(guesses)

            if(gameBoard.matching(guesses)==True and guesses[0]!=guesses[1]):
                print("You got a match!\n--------------------------")
                gameBoard.flipCards(guesses)
            else: print("--------------------------")

            gameBoard.printBoard()

        self.endGame()

    def makeGuess(self):
        localGuesses = [-1,-1] #Default for when fguess not made yet
        localGuesses[0], localGuesses[1] = int(input("Position 1: "))-1, int(input("Position 2: "))-1
        print("") #New Line
        self.numGuesses+=1
        return localGuesses

    def getBoardSize(self):
        size = int(input("Board Size: "))-1
        print("--------------------------")
        if(size%2==1): size+=1
        return size

    def endGame(self): print("You solved the board in {} guesses".format(self.numGuesses))

        
class Card:  
    def __init__(self,value): self.cardValue, self.isMatched = value, False

    def isMatched(self): return self.isMatched

    def getValue(self): return self.cardValue
    
    def flip(self):
        if not self.isMatched: self.isMatched=True
        else: self.isMatched=False

GameRunner()
