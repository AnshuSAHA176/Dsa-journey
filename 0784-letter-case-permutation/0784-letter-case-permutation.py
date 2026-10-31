class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        def solved(n:int,char:str):
            
            if n==len(s):
                result.append(char)
                return
                    
        
            solved(n+1,char=char+s[n])
            if  s[n].isalpha():
                if s[n].isupper():
                  solved(n+1,char=char+s[n].lower())

                else:
                    
                    solved(n+1,char=char+s[n].upper())
        solved(n=0,char='')
        return result