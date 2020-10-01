class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        try:
            return sorted(set(nums),reverse=True)[2]
        except:
            return sorted(nums)[-1]
        