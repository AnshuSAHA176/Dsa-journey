import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        result=0
        
        while (left <= right):
            hours=0
            mid = left + (right - left) // 2
            for pile in piles:
                hours += math.ceil(pile/mid)
           
            if hours<=h:
                result = mid
                right=mid-1
            elif hours > h:
                left = mid+1
                
            
        return result