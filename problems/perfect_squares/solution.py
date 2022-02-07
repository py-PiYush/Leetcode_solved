class Solution:
    def numSquares(self, n: int) -> int:
        
        ''' math '''
        if int(sqrt(n))**2 == n: return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j*j))**2 == n - j*j: return 2
            
        while n % 4 == 0: 
            n >>= 2
        if n % 8 == 7: return 4
        return 3
        
        
        ''' DP -> Similar to Coin change '''
        squares=[i*i for i in range(1,n+1)]
        dp=[0]+[float('inf')]*n
        for sq in squares:
            for i in range(sq, n+1):
                dp[i]=min(dp[i], 1+dp[i-sq])
        return dp[n]