class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]
        def solved(opening,closing,st:str):
            if opening>=n and closing>=n:
                result.append(st)
                return
            if opening<n:
                solved(opening=opening+1,closing=closing,st=st+"(")
            if closing<opening:
                solved(opening=opening,closing=closing+1,st=st+")")
            
        solved(opening=0,closing=0,st="")
        return result