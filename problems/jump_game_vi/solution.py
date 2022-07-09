class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        d = deque([(nums[0],0)])
        for i in range(1, len(nums)):
            dp[i] = nums[i] + d[0][0]
            
            while d and d[-1][0] < dp[i]:
                d.pop()
            d.append((dp[i],i))            
            
            if i-k == d[0][1]:              
                d.popleft()                 
                
        return dp[-1]
        
        ''' Recursion + memoization (TLE)'''
        @lru_cache(None)
        def recur(idx):
            if idx>=len(nums)-1:
                return nums[-1]
            score = -float('inf')
            for i in range(1, k+1):
                score = max(score, nums[idx] + recur(idx+i))
            return score
        return recur(0)