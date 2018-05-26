# Minesweeper Algorithm
Simple iterative solution to counts mines in [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game))

## Usage
- Provide a 2D list of a rectangular board with **`-1` representing a mine** and `0` in all other spaces
- call `displayMines(board)` passing in the board and the number of mines adjacent to each square will be printed preserving mines as `-1`
- Works for non-square dimensions

## Algorithm
- Copies the board to a new board where the counts will reside
- Loops over all squares in the input board
- If a mine is encountered, it checks the 8 surrounding squares & increments the count in each square that isn't a mine
  - Surrounding squares are checked by a nested for loop, `xTemp` coordinates go from `x-1` to `x+1` & `yTemp` coordinates go from `y-1` to `y+1`
  - All coordinates are checked to make sure they don't go out of bounds of the edges of the board
  - The current square is skipped by also checking if the value at `board[ytemp]pxTemp]` is a mine before incrementing
  
  ## Runtime
  O(mn) for looping over the entire board  
  O(8) for checking surrounding squares  
  O(8*mn) combined
  ⇒ **O(mn)**
