class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [["."] * n for _ in range(n)]
        result = []
        def isSafe(board: list, row: int, col: int) -> bool:
            # vertical up
            for i in range(row - 1, -1, -1):
                if board[i][col] == "Q":
                    return False
            # diag left up
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # diag right up
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def solved(board: list, row: int):
            if row == len(board):
                result.append(["".join(r) for r in board])
                return

            for j in range(len(board)):
                if isSafe(board, row, j):
                    board[row][j] = "Q"
                    solved(board=board, row=row + 1)
                    board[row][j] = "."

        solved(board=board, row=0)
        return result