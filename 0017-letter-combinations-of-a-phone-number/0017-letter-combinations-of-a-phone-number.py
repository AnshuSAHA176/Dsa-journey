class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result =[]
        def solved(current:str,index:int):
            if index == len(digits):
              result.append(current)
              return
            letters=phone[digits[index]]
            for letter in letters:
                solved(current=current + letter,index=index+1)
            
        solved(index=0,current='',)
        return result