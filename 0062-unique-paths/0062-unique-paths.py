class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def solved(i,j,m,n):
            if i==m-1 and j==n-1:
                return 1
            elif i==m or j==n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            w1=solved(i=i+1,j=j,m=m,n=n)
            w2=solved(i=i,j=j+1,m=m,n=n)
            memo[(i,j)]= w1+w2
            return memo[(i,j)]
        memo={}
        return solved(i=0,j=0,m=m,n=n)