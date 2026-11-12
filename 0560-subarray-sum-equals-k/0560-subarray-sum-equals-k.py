class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n=len(nums)
        hash_map = {0: 1}
        prefix = [0] * n
        prefix[0] = nums[0]
        count=0
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
       
        for i in range(n):
            
            required = prefix[i] - k
           
            if required in hash_map:
                count+=hash_map[required]
            
            hash_map[prefix[i]] = hash_map.get(prefix[i], 0) + 1
       
        return count