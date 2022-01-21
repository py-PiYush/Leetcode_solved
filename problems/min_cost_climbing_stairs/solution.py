class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ''' bottom up (space optimized)'''
        if len(cost)<=2:
            return min(cost[0], cost[1])
        one_back, two_back = 0, 0
        for i in range(2, len(cost)+1):
            temp=one_back
            one_back=min(one_back + cost[i-1], two_back + cost[i-2])
            two_back=temp
        return one_back
        
        
        
        '''Bottom up (tabulation)'''
        if len(cost)<=2:
            return min(cost[0], cost[1])
        dp=[-1]*(len(cost)+1)
        dp[0]=0
        dp[1]=0
        for i in range(2, len(cost)+1):
            dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[len(cost)]
        
        
        '''Top down (memoization+recursion)'''
        def dp(i):
            if i<=1:
                return 0
            if i not in memo:
                memo[i]=min(cost[i-1]+dp(i-1), cost[i-2]+dp(i-2))
            return memo[i]
        memo={}
        return dp(len(cost))