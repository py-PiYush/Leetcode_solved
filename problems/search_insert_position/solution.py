class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except:
        #     for i in range(len(nums)):
        #         if nums[i]>target:
        #             return i
        #     return len(nums)
        
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return l
            
            
            