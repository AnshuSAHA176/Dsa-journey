class Solution:
    def search(self, nums: list[int], target: int) -> int:

        def solved(st:int,end:int):
            if st>end:
                return -1
            mid=st+(end-st)//2
            
            if nums[mid] == target:
                return mid
            if nums[st]<=nums[mid]:
                if nums[st]<=target<=nums[mid]:
                    return solved(st=st,end=mid-1)
                else:
                    return solved(st=mid+1,end=end)
            else:
                if nums[mid]<=target<=nums[end]:
                    return solved(st=mid+1,end=end)
                else:
                    return solved(st=st,end=mid-1)
        return solved(st=0,end=len(nums)-1)