class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, curSum = nums[0], 0
        
        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            result = max(result, curSum)
        
        return result
        