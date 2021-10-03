class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         result, curSum = nums[0], 0
        
#         for i in range(len(nums)):
#             if curSum < 0:
#                 curSum = 0
#             curSum += nums[i]
#             result = max(result, curSum)
        
#         return result
        
        for i in range(1,len(nums)):
            nums[i]=max(nums[i], nums[i]+nums[i-1])
        return max(nums)
        