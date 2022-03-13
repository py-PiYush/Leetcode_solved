class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        
        if len(nums)==1:
            if k%2==1:
                return -1
            else:
                return nums[0]
        if k==0: return nums[0]
        if k==1: return nums[1]
        if k==2: return max(nums[0], nums[2])
        
        if k >len(nums):
            return max(nums)
        
        return max(max(nums[:k-1]), nums[k] if k<len(nums) else float('-inf'))
        
        
        
        
        
        
        '''--------------'''
        self.max = -1
        
        def rec(nums, k, removed):
            if k==0:
                self.max = max(self.max, nums[0] if nums else -1)
                # print(self.max)
                return
            
            rec(nums[1:], k-1, removed+[nums[0]])
            for i in range(len(removed)):
                rec([removed[i]]+nums, k-1, removed[:i]+removed[i+1:])
        
        rec(nums, k, [])
        return self.max