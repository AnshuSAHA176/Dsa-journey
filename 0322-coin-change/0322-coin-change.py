class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        result = 0
        memo = {}
        def solved(current_sum: int):
         
            if current_sum == 0:
                
                return 0
            elif current_sum<0:
                return float("inf")
            count = float("inf")
            for coin in coins:
                if current_sum in memo:
                    return memo[current_sum]
                else:
                    count = min(count, 1 + solved(current_sum - coin))
            memo[current_sum] = count
            return count
            

        answer =solved( current_sum=amount)
        return -1 if answer==float('inf') else answer