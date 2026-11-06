class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[]
        def solved(start:int,end:int,subArray:list):
            if start==end:
                result.append(subArray.copy())
                return
            
            solved(start=start+1,subArray=subArray+[nums[start]],end=end)
            solved(start=start+1,subArray=subArray,end=end)
        solved(start=0,end=len(nums),subArray=[])
        return result