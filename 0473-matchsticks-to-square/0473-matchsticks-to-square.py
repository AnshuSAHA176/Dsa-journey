class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total=sum(matchsticks)
        matchsticks.sort(reverse=True)
        target =  total//4
        if total%4!=0:
            return False
        if matchsticks[0]>target:
            return False
        bucket=[0]*4
        def solved(index:int=0):
            nonlocal bucket
            if index==len(matchsticks):
                return True
            for i in range(4):
                if i>0 and bucket[i] == bucket[i-1]:
                    continue
                if bucket[i]+matchsticks[index] <=target:
                    bucket[i]+=matchsticks[index]
                    if solved(index=index+1):
                        return True
                    bucket[i]-=matchsticks[index]
            return False
        return solved()
