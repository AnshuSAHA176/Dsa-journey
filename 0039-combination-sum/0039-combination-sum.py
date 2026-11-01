class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        resullt=[]
        candidates.sort()
        def solved(index:int,current:list,remaining:list):
            if  remaining==0:
                resullt.append(current.copy())
                return 

            if index == len(candidates) or remaining < candidates[index]:
                    return
            current.append(candidates[index])
            solved(index=index,current=current,remaining=remaining-candidates[index])
            current.pop()
            solved(index=index+1,current=current,remaining=remaining)
            
        solved(index=0,current=[],remaining=target)
        return resullt