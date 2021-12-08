class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j=0
        for i,x in enumerate(nums):
            if j<i:
                return False
            j=max(j,i+x)
        return True
            