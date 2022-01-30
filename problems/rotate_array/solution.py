class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''Approach 1--> O(n)'''
#         k=k%len(nums)
#         result=nums[len(nums)-k:]+nums[:len(nums)-k]
#         for i in range(len(nums)):
#             nums[i]=result[i]
        
        '''Approach 2--> O(n*k)'''
        # k=k%len(nums)
        # for _ in range(k):
        #     last=nums.pop()
        #     nums.insert(0,last)
        
        
        '''Reversion'''
        def numReverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k, n = k % len(nums), len(nums)
        if k:
            numReverse(0, n - 1)
            numReverse(0, k - 1)
            numReverse(k, n - 1)