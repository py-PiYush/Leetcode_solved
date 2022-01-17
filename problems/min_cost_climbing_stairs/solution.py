class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''Bottom up (tabulation)'''
        if len(cost)<=1:
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