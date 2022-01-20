class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        ''' bottom up '''
        n=len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for __ in range(n + 1)]
        
        for i in range(n-1, -1, -1):
            for transactionsRem in range(1, k+1):
                for holding in range(2):
                    do_nothing = dp[i+1][transactionsRem][holding]
                    if holding: #sell stock
                        do_something = prices[i] + dp[i+1][transactionsRem-1][0]
                    else: #buy stock
                        do_something = -prices[i] + dp[i+1][transactionsRem][1]
                    
                    dp[i][transactionsRem][holding] = max(do_nothing, do_something)
            
        return dp[0][k][0]
        
        
        
        ''' top down '''
        @lru_cache(None)
        # State variables
        # i -> ith day
        # transactionsRem -> how many transactions we have left
        # holding -> if we are holding on a stock
        def dp(i, transactionsRem, holding):
            
            #base case
            if transactionsRem == 0 or i==len(prices):
                return 0
            
            #recurrence relation
            do_nothing = dp(i+1, transactionsRem, holding)
            do_something = 0
            
            if holding:
                # Sell stock
                do_something = prices[i] + dp(i+1, transactionsRem -1, 0)
            
            else:
                # Buy stock
                do_something = -prices[i] + dp(i+1, transactionsRem, 1)
            
            return max(do_nothing, do_something)
        
        return dp(0, k, 0)