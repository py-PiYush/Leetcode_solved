class Solution:
    def tribonacci(self, n: int) -> int:
        '''space optimized'''
        if n==0: return 0
        if n<3: return 1
        
        cur, prev, prevPrev = 1, 1, 0
        for i in range(n-2):
            cur, prev, prevPrev = cur+prev+prevPrev, cur,prev
        return cur
        
        
        
        '''tabulation'''
        if n==0: return 0
        if n<3: return 1
        dp=[0]*(n+1)
        dp[1], dp[2] = 1, 1
        for i in range(3, n+1):
            dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
        return dp[n]
        
        
        '''memoization'''
        def dp(i):
            if i not in memo:
                memo[i]=dp(i-1)+dp(i-2)+dp(i-3)
            return memo[i]
        memo={0:0, 1:1, 2:1}
        return dp(n)