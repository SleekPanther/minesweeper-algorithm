#Count the number of mines
#-1 is a mine, positive numbers represent the number of mines touching a square

MINE_FLAG = -1

def displayMines(inputBoard):
    board=[]
    for row in inputBoard:
        board.append([0]*len(row))

    for i in range(len(inputBoard)):
        for j in range(len(inputBoard[i])):
            if inputBoard[i][j] == MINE_FLAG:   #found a mine
                if i-1 >= 0:        #left
                    board[i-1][j]+=1
                if i+1 < len(inputBoard[i]):    #right
                    board[i+1][j]+=1
                if j-1 >= 0:        #above
                    board[i][j-1]+=1
                if j+1 < len(inputBoard):       #below
                    board[i][j+1]+=1

                if i-1 >= 0 and j-1 >= 0:    #diagonal top left
                    board[i-1][j-1]+=1
                if i+1 < len(inputBoard[i]) and j+1 < len(inputBoard):    #diagonal bottom right
                    board[i+1][j+1]+=1
                if i+1 < len(inputBoard[i]) and j-1 >= 0:    #diagonal top right
                    board[i+1][j-1]+=1
                if i-1 < len(inputBoard[i]) and j+1 < len(inputBoard):    #diagonal bottom left
                    board[i-1][j+1]+=1

    #overwrite actual mine positions
    for i in range(len(inputBoard)):
        for j in range(len(inputBoard[i])):
            if inputBoard[i][j] == MINE_FLAG:
                board[i][j] = MINE_FLAG
        
    printBoard(board)
    

def printBoard(board):
    for row in board:
        print(row)


board=[[0,0,-1],
       [0,-1,-1],
       [0,0,-1]]

print('original board')
printBoard(board)
print('answers')
displayMines(board)
