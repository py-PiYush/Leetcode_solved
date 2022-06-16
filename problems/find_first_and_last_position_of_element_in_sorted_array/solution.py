class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        return [self.findFirst(nums, target), self.findSecond(nums, target)]
    
    
    def findFirst(self, nums, target):
        left, right = 0, len(nums)-1
        while left<right:
            mid = left + (right-left)//2
            if nums[mid]>=target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left]==target else -1
    
    def findSecond(self, nums, target):
        left, right = 0, len(nums)
        while left<right:
            mid = left + (right-left)//2
            if nums[mid]>target:
                right = mid
            else:
                left = mid + 1
        return left - 1  if nums[left-1]==target else -1