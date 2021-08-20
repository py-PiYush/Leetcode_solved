class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt=nums.count(0)
        if cnt==len(nums) or cnt==0:
            return
        idx=nums.index(0)
        i=idx
        for j in range(idx+1, len(nums)):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
        nums[len(nums)-cnt:]=[0]*cnt
        
#         pos = 0
        
#         for i in range(len(nums)):
#             el = nums[i]
#             if el != 0:
#                 nums[pos], nums[i] = nums[i], nums[pos]
#                 pos += 1