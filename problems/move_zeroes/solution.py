class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''j=len(nums)-1
        i=len(nums)-1
        while i>=0:
            if nums[i]==0:
                tmp=nums[j]
                nums[j]=0
                nums[i]=tmp
                j-=1
            i-=1'''
    
        i=0
        stop=nums.count(0)
        
        while i<len(nums)-stop:
            if nums[i]==0:
                nums.append(0)
                del nums[i]
                continue
            i+=1
        