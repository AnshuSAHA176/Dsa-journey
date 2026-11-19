class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result=[]
        def solved(start:int,current:list,number_needed:int):
            if number_needed == 0:
                result.append(current.copy())
                return 

            for i in range(start,n+1):
                current.append(i)
                solved(start=i+1,current=current,number_needed=number_needed-1)
                current.pop()

        solved(start=1,current=[],number_needed=k)
        return result