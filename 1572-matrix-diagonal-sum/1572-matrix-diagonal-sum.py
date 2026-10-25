class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        row=0
        col=0
        row_len=len(mat)
        col_len=len(mat[0])
        sum=0
        while(row<=row_len and col<col_len):
            sum+=mat[row][col]
            row+=1
            col+=1
        row=0
        col=col_len-1
        while (row<row_len and col<col_len):
            if row==col:
                row+=1
                col-=1
                continue
            sum+=mat[row][col]
            row+=1
            col-=1
        return sum
