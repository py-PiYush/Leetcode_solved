class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        sumUp, sumLeft = float('inf'), float('inf')
        for row in range(m):
            for col in range(n):
                if row>0:
                    sumUp = dp[row-1][col]
                if col>0:
                    sumLeft = dp[row][col-1]
                if row+col!=0:
                    dp[row][col]+=grid[row][col]+min(sumLeft, sumUp)
        # print(dp)
        return dp[-1][-1]