class Solution:
    def jump(self, nums: List[int]) -> int:
        
        '''Greedy'''
        l,r=0,0
        jumps=0
        while r<len(nums)-1:
            jumps+=1
            furthest=max(i+nums[i] for i in range(l, r+1))
            l,r=r+1,furthest
            
        return jumps
    
    
    
        ''' DP -> O(n^2)'''
        n=len(nums)
        dp=[0]+[float('inf')]*n
        
        for i in range(1,n):
            for j in range(i+1):
                if i<=j+nums[j]:
                    dp[i]=min(dp[i], dp[j]+1)
        # print(dp)
        return dp[n-1]