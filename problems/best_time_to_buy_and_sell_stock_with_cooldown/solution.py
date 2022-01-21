class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' bottom up '''
        n=len(prices)
        dp=[[0]*2 for _ in range(n+2)]
        
        for i in range(n-1, -1, -1):
            for holding in range(2):
                do_nothing = dp[i+1][holding]
                
                if holding:
                    do_something=prices[i] + dp[i+2][0]
                else:
                    do_something = -prices[i] + dp[i+1][1]
        
                dp[i][holding] = max(do_something, do_nothing)
        return dp[0][0]
        
        
        
        ''' top down '''
        @lru_cache(None)
        def dp(i, holding):
            #base case
            if i>=len(prices):
                return 0
            
            do_nothing = dp(i+1, holding)
            do_something =0
            
            if holding:
                #sell Stock
                do_something = prices[i] + dp(i+2, 0)
            else:
                do_something = -prices[i] + dp(i+1, 1)
            
            return max(do_something, do_nothing)
        
        return dp(0,0)