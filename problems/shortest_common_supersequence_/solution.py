class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        res = ''
        i, j =0, 0
        for ch in self.lcs(str1, str2):
            while str1[i]!=ch:
                res+=str1[i]
                i+=1
            while str2[j]!=ch:
                res+=str2[j]
                j+=1
            res+=ch
            i+=1
            j+=1
        return res + str1[i:] + str2[j:]
    
    def lcs(self, str1, str2):
        m, n = len(str1), len(str2)
        dp = [['' for _ in range(n+1)] for __ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)
        # print(dp)
        return dp[m][n]