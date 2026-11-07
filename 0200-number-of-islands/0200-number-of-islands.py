class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows,cols=len(grid),len(grid[0])
        count=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1':
                    count+=1
                    self.dfs(grid=grid,row=row,col=col)
        return count
    def dfs(self, grid: list[list[str]], row: int, col: int):

        if (
            (row < 0 or row >= len(grid))
            or (col < 0 or col >= len(grid[0]))
            or (grid[row][col] == "0")
        ):
            return

        grid[row][col] = "0"
        self.dfs(grid=grid, row=row - 1, col=col)
        self.dfs(grid=grid, row=row + 1, col=col)
        self.dfs(grid=grid, row=row, col=col - 1)
        self.dfs(grid=grid, row=row, col=col + 1)