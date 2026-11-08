class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
                    return 0
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    
                    area = self.naibourn(grid=grid, row=row, col=col)
                    max_area=max(max_area,area)
        return max_area
    def naibourn(self,grid: list[list[int]], row: int, col: int):
        if (
            row < 0 or row >= len(grid)
            or col < 0 or col >= len(grid[0])
            or grid[row][col] == 0
        ):
            return 0
            
        grid[row][col] = 0
        area=1
        area+=self.naibourn(grid=grid, row=row - 1, col=col)
        area+=self.naibourn(grid=grid, row=row + 1, col=col)
        area+=self.naibourn(grid=grid, row=row, col=col - 1)
        area+=self.naibourn(grid=grid, row=row, col=col + 1)
        return area