class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        hash_map = {0: 1}
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        count=0
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        print(prefix)
        for i in range(len(nums)):
            
            required = prefix[i] - k
            print(required)
            if required in hash_map:
                count+=hash_map[required]
            
            hash_map[prefix[i]] = hash_map.get(prefix[i], 0) + 1
        print(hash_map)
        return count