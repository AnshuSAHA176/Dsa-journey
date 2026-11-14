class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        n=len(candidates)
        def solved(index: int, current_sum: list, remaining: int):
            
            if remaining == 0:
                result.append(current_sum.copy())
                return
            if index >= n:
                return
            for i in range(index,n):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                current_sum.append(candidates[i])

                solved(i + 1, current_sum, remaining - candidates[i])

                current_sum.pop()

        solved(index=0, current_sum=[], remaining=target)
        return result