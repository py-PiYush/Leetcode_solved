class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''bottom up'''
        m, n = len(text1), len(text2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        print(dp)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1], dp[i-1][j])
        
        return dp[m][n]
        
        
        
        '''top down'''
        @lru_cache(None)
        def dp(i,j):
            #base case
            if i<0 or j<0:
                return 0
            #recurrence relation
            if text1[i]==text2[j]:
                return 1 + dp(i-1, j-1)
            return max(dp(i, j-1), dp(i-1, j))
        
        m, n = len(text1), len(text2)
        return dp(m-1, n-1)