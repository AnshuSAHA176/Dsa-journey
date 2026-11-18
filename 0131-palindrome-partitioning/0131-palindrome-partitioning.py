class Solution:

    def partition(self, s: str) -> list[list[str]]:
        result=[]
        def isPalindrome(substr:str)->bool:
          
            i=0
            j=len(substr)-1
            while i<=j:
                if substr[i]!=substr[j]:
                    return False
                i+=1
                j-=1
            return True
        def solved(start:int,current:list):
            if start==len(s):
                result.append(current.copy())
                return
            for end in range(start,len(s)):
                substr=s[start:end+1]
                if isPalindrome(substr=substr):
                    current.append(substr)
                    solved(start=end+1,current=current)
                    current.pop()
        solved(start=0,current=[])
        return result