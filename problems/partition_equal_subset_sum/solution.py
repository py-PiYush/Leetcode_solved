class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # target, n = sum(nums), len(nums)
        # if target & 1: return False
        # target >>= 1
        # dp = [True] + [False]*target
        # for x in nums:
        #     dp = [dp[s] or (s >= x and dp[s-x]) for s in range(target+1)]
        #     if dp[target]: return True
        # return False

    
        '''------------------'''
        total, n = sum(nums), len(nums)
        
        #check if total is odd (equal sum partition not possible)
        if total & 1 : return False
        
        #else subset sum problem
        target = total // 2
        dp = [[False]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
        
        for i in range(1,n+1):
            for j in range(1, target+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                    

        return dp[n][target]