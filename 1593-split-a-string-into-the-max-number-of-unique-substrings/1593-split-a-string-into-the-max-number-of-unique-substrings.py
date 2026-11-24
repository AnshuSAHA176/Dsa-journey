class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        count = 0
        seen={}

        def solved(index: int, current: list):
            if index >= len(s):
                nonlocal count
                
                count =max(count,len(current))

                return
            for end in range(index+1,len(s)+1):
                sub=s[index:end]
                if sub in seen:
                    continue
                seen[sub]=0
                current.append(sub)
                solved(index=end,current=current)
                current.pop()
                seen.pop(sub)
                
                
        solved(index=0,current=[])
        return count
