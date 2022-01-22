class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ''' bottom up '''
        dp=[1] + [0]*amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]+=dp[i-coin]
        return dp[amount]
        
        
        ''' top down '''
        @lru_cache(None)
        def dp(amount, coins):
            #base case
            if amount == 0: return 1
            if amount<0 or len(coins)==0:
                return 0
            
            #recurrence relation
            return dp(amount-coins[-1], coins) + dp(amount, coins[:-1])
        return dp(amount, tuple(coins))