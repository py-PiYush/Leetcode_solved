class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        '''bottom up'''
        n,m=len(nums), len(multipliers)
        dp=[[0]*(m+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                mult=multipliers[i]
                right=n-1-(i-left)
                dp[i][left]=max(nums[left]*mult + dp[i+1][left+1], 
                                nums[right]*mult + dp[i+1][left])
        
        return dp[0][0]
        
        '''top down'''
        @lru_cache(2000)
        def dp(i,left):
            
            #base case
            if i==m:
                return 0
            mult=multipliers[i]
            right=n-1-(i-left)
            
            #reccurence relation
            return max(nums[left]*mult + dp(i+1, left+1), nums[right]*mult + dp(i+1, left))
        
        n,m = len(nums), len(multipliers)
        return dp(0,0)