class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        ''' bottom up '''
        dp=[False]*(n+1)
        # dp[1]=True
        for i in range(1, n+1):
            for j in range(int(sqrt(i)), 0, -1):
                if j*j<=i and dp[i-j*j]==False:
                    dp[i]=True
                    break
        
        print(dp)
        return dp[n]
        
        
        
        '''top down'''
        @lru_cache(None)
        def dp(remain):
            
            #base cases
            if remain==0: return False
            if remain==1: return True
            
            #recurrence relation
            for i in range(1, int(sqrt(remain))+1):
                if not dp(remain - i*i):
                    return True
                
            return False
        return dp(n)
                