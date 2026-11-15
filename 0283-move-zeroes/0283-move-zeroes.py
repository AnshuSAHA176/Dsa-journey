class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsOfZero=0
        i=0
        while i<len(nums):
            if nums[i]==0:
                nums.pop(i)
                numsOfZero+=1
            else:
                i+=1
        for _ in range(numsOfZero):
            nums.append(0)
      
        