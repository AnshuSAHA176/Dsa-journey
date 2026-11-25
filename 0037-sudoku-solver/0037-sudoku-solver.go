func solveSudoku(board [][]byte) {

    isSafe := func(sudoku [][]byte, row, col int, digit byte) bool {

        // Check column
        for i := 0; i < 9; i++ {
            if sudoku[i][col] == digit {
                return false
            }
        }

        // Check row
        for i := 0; i < 9; i++ {
            if sudoku[row][i] == digit {
                return false
            }
        }

        // Check 3x3 box
        sr := (row / 3) * 3
        sc := (col / 3) * 3

        for i := sr; i < sr+3; i++ {
            for j := sc; j < sc+3; j++ {
                if sudoku[i][j] == digit {
                    return false
                }
            }
        }

        return true
    }

    
    var sudokuSolver func(int,int)bool
    sudokuSolver = func(row, col int) bool {

        // All rows completed
        if row == 9 {
            return true
        }

        nextRow := row
        nextCol := col + 1

        if nextCol == 9 {
            nextRow++
            nextCol = 0
        }

        // Skip already filled cells
        if board[row][col] != '.' {
            return sudokuSolver(nextRow, nextCol)
        }

        // Try digits 1 to 9
        for digit := byte('1'); digit <= '9'; digit++ {

            if isSafe(board, row, col, digit) {

                board[row][col] = digit

                if sudokuSolver(nextRow, nextCol) {
                    return true
                }

                // Backtrack
                board[row][col] = '.'
            }
        }

        return false
    }

    sudokuSolver(0, 0)
}
