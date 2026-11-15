class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsOfZero=0
        i=0
        j=0
        while i<len(nums):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
            i+=1
        while j < len(nums):
            nums[j] = 0
            j += 1