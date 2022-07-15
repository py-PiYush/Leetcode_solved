class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        ''' dp '''
        # dp[i][j] denotes lps of s[i:j+1]
        n=len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i]==s[j]:
                    dp[i][j] = 2+ dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
        
        
        ''' BAsed on LCS'''
        return self.longestCommonSubsequence(s, s[::-1])
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]