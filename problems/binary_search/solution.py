class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left, right = 0, len(nums)-1
        # while left < right:
        #     mid = left + (right-left)//2
        #     if target <= nums[mid]:
        #         right = mid
        #     else:
        #         left = mid+1
        # print(left)
        # return left if nums[left]==target else -1
        
        
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                hi=mid-1
            else:
                lo=mid+1
        return -1