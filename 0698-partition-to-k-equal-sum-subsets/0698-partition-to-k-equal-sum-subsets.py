class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total=sum(nums)
        if total%k !=0:
            return False
        target = total //k
        nums.sort(reverse=True)
        if nums[0]>target:
            return False
        bucket=[0]*k
        
        def solved(index: int):
            if index==len(nums):
                return True
            for i in range(k):
                if i > 0 and bucket[i] == bucket[i - 1]:
                    continue
                if bucket[i]+nums[index] <= target:
                    bucket[i]+=nums[index]
                
                    if solved(index + 1):
                        return True
                    bucket[i]-=nums[index]
            return False
            
        return solved(index=0)