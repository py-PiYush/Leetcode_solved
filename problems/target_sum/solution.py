class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total, n = sum(nums), len(nums)
        if (total+target)%2 or abs(target)>total: return 0
        tgt = (total+target)//2
        dp=[[0]*(tgt+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
            
        for i in range(1, n+1):
            for j in range(tgt+1):
                if nums[i-1]<=j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        print(dp)
        return dp[n][tgt]