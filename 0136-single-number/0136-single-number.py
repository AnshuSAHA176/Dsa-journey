class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums)==0:
            return nums[0]
        
        result=0
        for num in nums:
            result = result^num
        return result