class Solution:
    def rob(self, nums: list[int]) -> int:
       memo = {}
       def solved(i):
        
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            rob = nums[i] + solved(i + 2)
            skip = solved(i + 1)

            memo[i] = max(rob, skip)
            return memo[i]
       return solved(i=0)