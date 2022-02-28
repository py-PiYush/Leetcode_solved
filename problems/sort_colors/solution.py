class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start, move, end = 0, 0, len(nums)-1
        while move<=end:
            if nums[move]<1:
                nums[move], nums[start] = nums[start], nums[move]
                start+=1
                move+=1
            elif nums[move]>1:
                nums[move], nums[end] = nums[end], nums[move]
                end-=1
            else:
                move+=1
        return nums