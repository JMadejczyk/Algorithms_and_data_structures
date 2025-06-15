sudoku = [
    [".", ".", "6", ".", "1", ".", "3", "5", "4"],
    ["8", "5", "1", "4", ".", "3", "7", ".", "."],
    [".", ".", "3", "5", "6", ".", "8", ".", "."],
    [".", "1", ".", ".", ".", ".", "5", "8", "3"],
    ["6", ".", "5", ".", "2", "1", "4", "9", "."],
    ["7", ".", "4", ".", ".", ".", ".", ".", "6"],
    ["5", ".", ".", ".", ".", "4", "9", ".", "."],
    ["3", ".", "2", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", "8", ".", ".", ".", ".", "5"],
]

# for checking purposes only
solved_sudoku = [
 ['9', '2', '6', '7', '1', '8', '3', '5', '4'],
 ['8', '5', '1', '4', '9', '3', '7', '6', '2'],
 ['4', '7', '3', '5', '6', '2', '8', '1', '9'],
 ['2', '1', '9', '6', '4', '7', '5', '8', '3'],
 ['6', '8', '5', '3', '2', '1', '4', '9', '7'],
 ['7', '3', '4', '9', '8', '5', '1', '2', '6'],
 ['5', '6', '8', '2', '7', '4', '9', '3', '1'],
 ['3', '4', '2', '1', '5', '9', '6', '7', '8'],
 ['1', '9', '7', '8', '3', '6', '2', '4', '5']
]

class Sudoku:
    def __init__(self, board):
        self.board = board
        
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ".":
                    return i, j
        return None, None
        
    
    def is_valid(self, num, row, col):
        if num in self.board[row]:
            return False

        if num in [self.board[i][col] for i in range(9)]:
            return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
        return True
  
    def solve_sudoku(self):
        row, col = self.find_empty()
        if row == None:
            return True
        for n in map(str, range(1,10)): 
            if self.is_valid(n, row, col):
                self.board[row][col] = n
                if self.solve_sudoku():
                    return True
                self.board[row][col] = "."
        return False

    def print_board(self):
        for row in self.board:
            print(*row)
        
sudoku = Sudoku(sudoku)
if sudoku.solve_sudoku():
    print("Sudoku solved")
    sudoku.print_board()
