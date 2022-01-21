class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ''' bottom up'''
        dp=[0]+[float('inf')]*amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]=min(dp[i], 1 + dp[i-coin])
        print(dp)
        return dp[amount] if dp[amount]!=float('inf') else -1
        
        
        
        '''top down'''
        @lru_cache(None)
        def dp(i): #return fewest number of coins to make up 'i' money
            
            #base case
            if i==0:
                return 0
            
            fewest=float('inf')
            for coin in coins:
                if i-coin>=0:
                    fewest=min(fewest, 1 + dp(i-coin))
            return fewest
        
        ans = dp(amount)
        return ans if ans!=float('inf') else -1
            