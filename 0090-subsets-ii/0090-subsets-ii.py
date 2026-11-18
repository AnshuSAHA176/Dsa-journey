class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        def solved(start:int,current:list):
            result.append(current.copy())
            for i in range(start,len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                solved(start=i+1,current=current)
                current.pop()

        solved(start=0,current=[])
        return result