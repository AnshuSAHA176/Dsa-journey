class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def solved(index,current):
         
            if index==len(nums):
                
                result.append(current.copy())
                return current
            solved(index+1,current=current+[nums[index]])
            solved(index=index+1,current=current)
            
            return current
        solved(index=0,current=[])
        return result