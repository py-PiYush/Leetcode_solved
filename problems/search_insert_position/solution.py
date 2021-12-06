class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except:
        #     for i in range(len(nums)):
        #         if nums[i]>target:
        #             return i
        #     return len(nums)
        
        l,r=0,len(nums)
        while l<r:
            mid=l+ (r-l)//2
            if nums[mid]>=target:
                r=mid
            else:
                l=mid+1
        return l
        
            
            
            