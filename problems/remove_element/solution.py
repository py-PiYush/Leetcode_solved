class Solution:

        
    def removeElement(self, nums: List[int], val: int) -> int:
        n=nums.count(val)
        for i in range(len(nums)):
            if nums[i]==val:
                j=i
                while j>0:
                    nums[j]=nums[j-1]
                    j-=1
        
        del nums[:n]
        