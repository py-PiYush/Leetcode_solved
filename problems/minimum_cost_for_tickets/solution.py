class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        backward
        dp[i] represents the cost you need if day i is 
        the first day in your travel plan. In other words,
        the cost if you travel from day i to day 365.
        If you do not travel on day i, dp[i] = dp[i+1];
        If you DO traverl on day i, dp[i] = min(dp[i+1] + costs[0], dp[i+7] + costs[1] +
        dp[i+30]+ costs[2])
        '''
        dp=[0]*367
        dayset=set(days)
        for i in range(365, 0, -1):
            if i not in dayset:
                dp[i]=dp[i+1]
            else:
                dp[i]=min(dp[min(i+d, 366)] + c for c, d in zip(costs, [1,7,30]) )
        
        return dp[1]
        
        
        
        
        '''
        2. forward
        dp[i] represents the cost you need if day i 
        is the i-th day in your traverl plan. In other words,
        the cost if you traverl from day 1 to day i.
        If you do not travel on day i, dp[i] = dp[i-1].
        If you DO traverl on day i, dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1] +
        dp[i-30] + costs[2]).
        '''
        dp=[0]*366
        dayset = set(days)
        for i in range(1, 366):
            if i not in dayset:
                dp[i]=dp[i-1]
            else:
                dp[i]=min(dp[max(0,i-d)] + c for c, d in zip(costs, [1, 7, 30]))
        
        return dp[365]
        
        
        
        ''' top down '''
        @lru_cache(None)
        def dp(i):  #min cost travelling from i --> last day
            
            #base case
            if i>365:
                return 0
            
            #travelling on a day
            elif i in dayset:
                return min(dp(i+d) + c for c, d in zip(costs, [1, 7, 30]))
            
            #not travelling
            else:
                return dp(i+1)
        
        dayset=set(days)
        return dp(days[0])