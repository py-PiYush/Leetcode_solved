class Solution:
    def rob(self, nums: List[int]) -> int:
        '''Space optimized'''
        cur, prev, prev2=0,0,0
        for n in nums:
            cur=max(prev, n+prev2)
            prev2=prev
            prev=cur
        return cur
        
        
        ''' Bottom up'''
        if len(nums)==1:
            return nums[0]
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        dp[1]=max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i]=max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]
        
        
        
        
        '''Top down'''
        def dp(i):
            #Base cases
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i]=max(dp(i-1), dp(i-2)+nums[i])
            return memo[i]
        
        memo={}
        return dp(len(nums)-1)
    
    