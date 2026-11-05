class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result=[]
        def solved(numbers:list,current:list):
            if len(numbers) == 0:
                result.append(current.copy())
                return 
            for i in range(len(numbers)):
                curr=numbers[i]
                sub_list=numbers[0:i]+numbers[i+1:]

                solved(numbers=sub_list,current=current+[curr])
            return current
        solved(numbers=nums,current=[])
        return result

