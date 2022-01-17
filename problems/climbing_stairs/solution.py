class Solution:
    
    
    def __init__(self):
        self.dic = {1:1, 2:2}
    
    def climbStairs(self, n):
        
        '''Bottom up dp'''
        if n==1: return 1
        dp=[0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        
        
        '''Top down dp'''
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]
    
    
    
    
    # def climbStairs(self, n: int) -> int:
    #     def fibonacci(n):
    #         if n==0 or n==1:
    #             return n
    #         a,b=0,1
    #         for _ in range(n):
    #             a,b=b,b+a
    #         return a
    #     return fibonacci(n+1)