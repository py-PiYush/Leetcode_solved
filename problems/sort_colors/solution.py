class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.dnf(nums)
        
    def dnf(self,nums):
        def swap(nums,i,j):
            nums[i],nums[j]=nums[j],nums[i]
            
        start,white=0,0
        pivot=1
        end=len(nums)-1
        while white<=end:
            if nums[white]<pivot:
                swap(nums,start,white)
                start+=1
                white+=1
                
            elif nums[white]>pivot:
                swap(nums,white,end)
                end-=1
            else:
                white+=1
                
                
            
#         def insertion(nums):
#             for i in range(1,len(nums)):
#                 key=nums[i]
#                 j=i-1
#                 while j>=0 and key<nums[j]:
#                     nums[j+1]=nums[j]
#                     j-=1
#                 nums[j+1]=key
            
#         insertion(nums)
                    