class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        def solved(start:int,number_need:int,remaining:int,current:list):
            if number_need==0:
                if remaining==0:
                    result.append(current.copy())
                return
            for i in range(start,10):
                if i > remaining:
                    break
                current.append(i)
                solved(start=i+1,number_need=number_need-1,remaining=remaining-i,current=current)
                current.pop()

        solved(start=1,number_need=k,remaining=n,current=[])
        return result