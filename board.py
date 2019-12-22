
class Board(object):
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.div = len(board) / 3
    
    def __str__(self):
        print('')
        for row in range(self.rows):
            if row % self.div == 0 and row != 0:
                print('- ' * (self.rows+5))

            for col in range(self.cols):
                if col % self.div == 0:
                    print(" | ", end="")
                    
                if col == self.rows-1:
                    print(self.board[row][col])
                else:
                    print(str(self.board[row][col]) + " ", end="")
        return ''


    def find_empty(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def valid(self, number, position):
        _row, _col = position

        # check row
        for col in range(self.cols):
            if self.board[_row][col] == number and _col != col:
                return False

        # check col
        for row in range(self.rows):
            if self.board[row][_col] == number and _row != row:
                return False

        # check box
        _x = _row // 3
        _y = _col // 3

        for row in range(_x * 3, _x * 3 + 3):
            for col in range(_y * 3, _y * 3 + 3):
                if self.board[row][col] == number and (row, col) != (_row, _col):
                    return False

        return True

    
    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for number in range(1, 10):
            if self.valid(number, (row, col)):
                self.board[row][col] = number

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False
