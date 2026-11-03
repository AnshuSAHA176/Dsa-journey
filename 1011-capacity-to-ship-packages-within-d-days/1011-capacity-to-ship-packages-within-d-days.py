class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
    
        left = max(weights)
        right = sum(weights)
        result = 0
        while left<=right:
           
            
            mid=left+(right-left)//2
            
            current_weight = 0
            required_days = 1
            
            for weight in weights:
                if current_weight+weight>mid:
                    current_weight = weight
                    required_days+=1
                else:
                    current_weight+=weight
                
           
            if required_days <= days:
                
                result=mid
                
                right=mid-1
               
                
            elif required_days >days:
                left=mid+1
                
        return result
