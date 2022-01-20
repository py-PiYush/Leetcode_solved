class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ''' binary search'''
        sub=[-float('inf')]
        for n in nums:
            if n>sub[-1]:
                sub.append(n)
            else:
                l, r = 0, len(sub)
                while l<r:
                    mid=l+(r-l)//2
                    if sub[mid]>=n:
                        r=mid
                    else:
                        l=mid+1
                sub[l]=n
        return len(sub)-1
        
        
        
        
        ''' bottom up '''
        dp=[1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j] and dp[i]<1 + dp[j]:
                    dp[i]=1+dp[j]
                    
        return max(dp)
        
        
        
        ''' top down '''
        @lru_cache(None)
        def dp(i):
            longest=1
            for j in range(i):
                if nums[i]>nums[j]:
                    longest=max(longest, 1+dp(j))
            return longest
        
        
        max_=-float('inf')
        for k in range(len(nums)):
            max_=max(max_, dp(k))
        return max_