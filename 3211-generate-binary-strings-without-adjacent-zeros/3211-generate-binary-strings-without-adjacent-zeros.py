class Solution:
    def validStrings(self, n: int) -> List[str]:
        result=[]
        def solved(n:int,char:str,lastPlace:int):
            if n==0:
                result.append(char)
                return
            solved(n=n-1,char=char+'1',lastPlace=1)
            if lastPlace==1:
                solved(n=n-1,char=char+'0',lastPlace=0)
        solved(n=n,char='',lastPlace=1)
        return result