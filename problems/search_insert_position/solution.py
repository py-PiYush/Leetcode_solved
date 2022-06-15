class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except:
        #     for i in range(len(nums)):
        #         if nums[i]>target:
        #             return i
        #     return len(nums)
        
        def condition(k):
            if nums[k]>=target:
                return True
            return False
        
        left, right = 0, len(nums)
        while left<right:
            mid = left + (right - left)//2
            if condition(mid):
                right=mid
            else:
                left=mid+1
        return left

    
        
        
            
            
            