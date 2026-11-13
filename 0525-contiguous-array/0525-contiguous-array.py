class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
     
        prefix_sum=[0]*len(nums)
        prefix_sum[0]=nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        
        hash_map = {0: -1}
        max_length = 0
        for i in range(len(nums)):
            if prefix_sum[i] in hash_map:
                lenght=i-hash_map[prefix_sum[i]]
                max_length = max(max_length,lenght)
            else:
                hash_map[prefix_sum[i]]=i

        return max_length