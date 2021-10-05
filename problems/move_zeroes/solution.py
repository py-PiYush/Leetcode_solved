class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
    
#         i=0
#         stop=nums.count(0)
        
#         while i<len(nums)-stop:
#             if nums[i]==0:
#                 nums.append(0)
#                 del nums[i]
#                 continue
#             i+=1
            
            
        pt1 = 0
        pt2 = 0
        n = len(nums)
        while(pt2<n):
            if (nums[pt2]!= 0):
                nums[pt1], nums[pt2] = nums[pt2], nums[pt1] # SWAP 
                pt1 += 1
            pt2 += 1