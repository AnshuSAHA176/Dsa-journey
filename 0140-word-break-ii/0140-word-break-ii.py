class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        result=[]
        wordDict=set(wordDict)
        def solved(index:int,current:list):
            if index==len(s):
                result.append(" ".join(current))
                return 
            for end in range(index+1,len(s)+1):
                word = s[index:end]
               
                if word in wordDict:
                    
                    current.append(word)
                    solved(index=end,current=current)
                    current.pop()
        solved(index=0,current=[])
        return result
            
                