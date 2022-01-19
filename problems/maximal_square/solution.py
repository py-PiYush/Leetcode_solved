class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        '''Bottom up dp'''
        
        m, n = len(matrix), len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        maxSqLen=0
        for col in range(n):
            if matrix[0][col]=='1':
                dp[0][col]=1
                maxSqLen = 1
        for row in range(m):
            if matrix[row][0]=='1':
                dp[row][0]=1
                maxSqLen=1
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]=='1':
                    dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    maxSqLen = max(maxSqLen, dp[i][j])
        
        return maxSqLen**2