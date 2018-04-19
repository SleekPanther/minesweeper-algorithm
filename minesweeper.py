#Count the number of mines
#-1 is a mine, positive numbers represent the number of mines touching a square

MINE_FLAG = -1

def displayMines(inputBoard):
	answerBoard=[]
	for row in inputBoard:
		newRow = []
		for cell in row:
			newRow.append(cell)
		answerBoard.append(newRow)

	bottomEdge = len(inputBoard) -1
	rightEdge = len(inputBoard[0]) -1

	for y in range(bottomEdge+1):
		for x in range(rightEdge+1):
			if inputBoard[y][x] == MINE_FLAG:   #found a mine
				#left
				if x-1 >= 0:
					if inputBoard[y][x-1] != MINE_FLAG:
						answerBoard[y][x-1]+=1
				#right
				if x+1 <= rightEdge:
					if inputBoard[y][x+1] != MINE_FLAG:
						answerBoard[y][x+1]+=1
				#below
				if y+1 <= bottomEdge:
					if inputBoard[y+1][x] != MINE_FLAG:
						answerBoard[y+1][x]+=1
				#above
				if y-1 >= 0:
					if inputBoard[y-1][x] != MINE_FLAG:
						answerBoard[y-1][x]+=1
				#diagonal top left
				if y-1 >= 0 and x-1 >= 0:
					if inputBoard[y-1][x-1] != MINE_FLAG:
						answerBoard[y-1][x-1]+=1
				#diagonal top right
				if y-1 >=0 and x+1 <= rightEdge:
					if inputBoard[y-1][x+1] != MINE_FLAG:
						answerBoard[y-1][x+1]+=1
				#diagonal bottom right
				if y+1 <= bottomEdge and x+1 <= rightEdge:
					if inputBoard[y+1][x+1] != MINE_FLAG:
						answerBoard[y+1][x+1]+=1
				#diagonal bottom left
				if y+1 <= bottomEdge and x-1 >= 0:
					if inputBoard[y+1][x-1] != MINE_FLAG:
						answerBoard[y+1][x-1]+=1

	printBoard(answerBoard)
	

def printBoard(board):
	for row in board:
		print(row)


board=[[0, 0,0],
	   [0,0,-1],
	   [0, -1, 0],
	   [-1,-1,0]]

print('Original board')
printBoard(board)

print('Answers')
displayMines(board)