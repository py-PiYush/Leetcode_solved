class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         ''' Memoization'''
#         def lcs(m, n):
#             if m==0 or n==0:
#                 return 0
#             if memo[m][n]!=-1:
#                 return memo[m][n]
#             if text1[m-1] == text2[n-1]:
#                 memo[m][n] = 1 + lcs(m-1, n-1)
#             else:
#                 memo[m][n] = max(lcs(m-1, n), lcs(m, n-1))
#             return memo[m][n]
        
#         m, n = len(text1), len(text2)
#         memo = [[-1 for _ in range(n+1)] for __ in range(m+1)]
#         return lcs(m,n)
    
        ''' Tabulation'''
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]