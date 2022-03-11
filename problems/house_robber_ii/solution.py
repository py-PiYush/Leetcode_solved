class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums):
            dp1, dp2 = 0, 0
            for num in nums:
                dp1, dp2 = dp2, max(dp1 + num, dp2)          
            return dp2
    
        return max(nums[0] + rob_helper(nums[2:-1]), rob_helper(nums[1:]))
        
        
        
        '''--------------'''
        n=len(nums)
        if n==1: return nums[0]
        if n==2: return max(nums)
        
        cur1, prev, prev2=0,0,0
        for n in nums[:n-1]:
            cur1=max(prev, n+prev2)
            prev2=prev
            prev=cur1
        
        cur2, prev, prev2 = 0, 0, 0
        for n in nums[1:]:
            cur2=max(prev, n+prev2)
            prev2=prev
            prev=cur2
            
        return max(cur1, cur2)