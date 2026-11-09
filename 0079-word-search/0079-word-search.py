class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def solved(row, col, word_idx):
            if word_idx == len(word):
                            return True
            if (
                row < 0 or row >= rows
                or col < 0 or col >= cols
                or board[row][col] == "#"
            ):
                return False
            
            if board[row][col] != word[word_idx]:
                
                return False
            
            original=board[row][col]
            
            board[row][col]="#"
            found= (
                    solved(row=row + 1, col=col, word_idx=word_idx + 1)
                    or solved(row=row - 1, col=col, word_idx=word_idx + 1)
                    or solved(row=row, col=col + 1, word_idx=word_idx + 1)
                    or solved(row=row, col=col - 1, word_idx=word_idx + 1)
                )
            board[row][col]=original
            return found

        for r in range(rows):
            for c in range(cols):
                if solved(r, c, 0):
                    return True

        return False