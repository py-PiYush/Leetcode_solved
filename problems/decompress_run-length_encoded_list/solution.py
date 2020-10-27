class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i=0
        res=[]
        while i<len(nums):
            freq=nums[i]
            val=nums[i+1]
            res+=[val]*freq
            i+=2
        return res