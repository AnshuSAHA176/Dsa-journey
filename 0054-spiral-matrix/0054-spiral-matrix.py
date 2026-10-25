class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result =[]
        start_row=0
        start_col=0
        end_row=len(matrix)-1
        end_col=len(matrix[0])-1
        while(start_row<=end_row and start_col<=end_col):
            #top row
            for col in range(start_col,end_col+1):
                result.append(matrix[start_row][col])
            start_row+=1
            #right col
            for row in range(start_row,end_row+1):
                result.append(matrix[row][end_col])
            end_col-=1
            # bottom row
            if start_row<=end_row:
                for col in range(end_col,start_col-1,-1):
                    result.append(matrix[end_row][col])
                end_row-=1
            #left col
            if start_col<=end_col:
                for row in range(end_row,start_row-1,-1):
                    result.append(matrix[row][start_col])
                start_col+=1
        return result


