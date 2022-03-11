class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j=0
        for i,x in enumerate(nums):
            if j<i:
                return False
            j=max(j,i+x)
        return True
        
        
        '''--------------------------'''
        n = len(nums)
        
        @lru_cache(None)
        def dp(i):
            if i == n - 1:
                return True
            
            for j in range(i+1, min(i+nums[i], n-1) + 1):
                if dp(j):
                    return True
            return False
        
        return dp(0)
            