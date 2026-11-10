class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=set()

        for i in range(len(nums)):
            seen=set()
            target=-(nums[i])
            # print(target)
            for j in range(i+1,len(nums)):
                complement=target-nums[j]
                if complement in seen:
                    triplet=tuple(sorted((nums[i],nums[j],complement)))
                    result.add(triplet)
                seen.add(nums[j])
        return [list(triplet) for triplet in result]