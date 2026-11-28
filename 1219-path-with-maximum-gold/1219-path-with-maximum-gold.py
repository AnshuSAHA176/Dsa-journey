class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        max_gold=float("-inf")
        rows=len(grid)
        cols=len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def solved(row:int,col:int,current:int):
            nonlocal max_gold
            max_gold=max(max_gold,current)
            gold=grid[row][col]
            grid[row][col]=0

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                    solved(nr, nc, current + grid[nr][nc])

            grid[row][col]=gold

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]>0:
                    solved(row=r,col=c,current=grid[r][c])

        return max_gold if max_gold != float('-inf') else 0
