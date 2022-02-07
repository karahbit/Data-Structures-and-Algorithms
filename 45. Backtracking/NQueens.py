class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]

    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    print("Q", end=' ')
                else:
                    print(".", end=' ')
            print()

    def is_place_safe(self, row, col):
        for j in range(col):
            if self.board[row][j] == 1:
                return False

        j = col
        for i in range(row, -1, -1):
            if j < 0:
                break
            if self.board[i][j] == 1:
                return False
            j -= 1

        j = col
        for i in range(row, self.n):
            if j < 0:
                break
            if self.board[i][j] == 1:
                return False
            j -= 1

        return True

    def solve(self, col):
        if col == self.n:
            return True

        for row in range(self.n):
            if self.is_place_safe(row, col):
                self.board[row][col] = 1
                if self.solve(col + 1):
                    return True
                self.board[row][col] = 0

        return False

    def solve_NQueens(self):
        if self.solve(0):
            self.print_board()
        else:
            print("Solution does not exist")


if __name__ == '__main__':
    n = 8
    nq = NQueens(n)
    nq.solve_NQueens()
