class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''Approach 1'''
#         k=k%len(nums)
#         result=nums[len(nums)-k:]+nums[:len(nums)-k]
#         for i in range(len(nums)):
#             nums[i]=result[i]
        
        '''Approach 2'''
        k=k%len(nums)
        for _ in range(k):
            last=nums.pop()
            nums.insert(0,last)