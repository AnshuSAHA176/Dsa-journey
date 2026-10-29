class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def solved(n):
            if n==0 or n==1:
                return 1
            if n in memo:
                return memo[n]
            
            memo[n]=solved(n-1)+solved(n-2)
            return memo[n]
        return solved(n)