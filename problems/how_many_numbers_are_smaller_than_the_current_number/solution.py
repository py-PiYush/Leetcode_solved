class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new=sorted(nums)
        return [new.index(i) for i in nums]