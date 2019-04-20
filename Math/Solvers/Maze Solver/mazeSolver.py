import numpy as np
from PIL import Image


def main(filename):
    newMaze = deadFill(filename)
    leftSolve(newMaze)

    
def deadFill(filename):
    maze = makeMaze(filename)
    h, w = np.shape(maze)
    oldMaze = np.zeros(maze.size)
    newImg = Image.new('L', (w, h))
    pixs = newImg.load()
    
    while not np.array_equal(maze, oldMaze):
        oldMaze = np.array(maze)
        for r in range(1, h - 1):
            for c in range(1, w - 1):
                edgeCounter = 0
                if(maze[r, c - 1] == 1): edgeCounter += 1
                if(maze[r, c + 1] == 1): edgeCounter += 1
                if(maze[r - 1, c] == 1): edgeCounter += 1
                if(maze[r + 1, c] == 1): edgeCounter += 1

                if(edgeCounter >= 3): maze[r, c] = 1

    for r in range(0, h):
        for c in range(0, w):
            if(maze[r, c] == 1): pixs[c, r] = 0
            else: pixs[c, r] = 255

    newFilename = filename[:-4] + "_new.bmp" 
    newImg.save(newFilename)
    return maze


def makeMaze(filename):
    mazeImg = Image.open(filename)
    h, w = mazeImg.size
    pixs = mazeImg.load()
    
    mazeArr = np.zeros((h, w), dtype=np.uint8)

    for r in range(0, w):
        for c in range(0, h):
            if(pixs[c, r] == 0):
                mazeArr[r, c] = 1
                
    return mazeArr


def leftSolve(maze):
    currentX, currentY = 1 , 0
    currentPos = (currentY, currentX)
    steps = 0
    heading = 'S'  # N,S,E,W
    
    while(currentY != np.size(maze, 0) - 1):
        # left, foward, right
        if heading == 'S':
            if(maze[currentY, currentX + 1] == 0):
                currentX += 1
                heading = 'E'
            elif(maze[currentY + 1, currentX] == 0):
                currentY += 1
                heading = 'S'
            elif(maze[currentY, currentX - 1] == 0):
                currentX -= 1
                heading = 'W'
            else:
                currentY -= 1
                heading = 'N'
                
        elif heading == 'E':
            if(maze[currentY - 1, currentX] == 0):
                currentY -= 1
                heading = 'N'
            elif(maze[currentY, currentX + 1] == 0):
                currentX += 1
                heading = 'E'
            elif(maze[currentY + 1, currentX] == 0):
                currentY += 1
                heading = 'S'
            else:
                currentX -= 1
                heading = 'W'

        elif heading == 'N':
            if(maze[currentY, currentX - 1] == 0):
                currentX -= 1
                heading = 'W'
            elif(maze[currentY - 1, currentX] == 0):
                currentY -= 1
                heading = 'N'
            elif(maze[currentY, currentX + 1] == 0):
                currentX += 1
                heading = 'S'
            else:
                currentY += 1
                heading = 'S'

        elif heading == 'W':
            if(maze[currentY + 1, currentX] == 0):
                currentY += 1
                heading = 'S'
            elif(maze[currentY, currentX - 1] == 0):
                currentX -= 1
                heading = 'W'
            elif(maze[currentY - 1, currentX] == 0):
                currentY -= 1
                heading = 'N'
            else:
                currentX += 1
                heading = 'E'
                
        currentPos = (currentY, currentX)
        steps += 1

    print("solved in {} steps".format(steps))

                    
main(input("Filename: "))
input("ENTER TO EXIT")
