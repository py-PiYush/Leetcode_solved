class Solution:
    def minSteps(self, n: int) -> int:
        ''' prime factorization '''
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
        
        
        
        ''' dp '''
        dp=[0]*(n+1)
        for i in range(2, n+1):
            dp[i]=i
            for j in range(i//2, 1, -1):
                if i%j == 0:
                    dp[i] = dp[j] + i//j
                    break
        return dp[n]
                    