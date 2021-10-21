class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i in range(len(nums)):
            if nums[i] in m:
                return m[nums[i]],i
            comp=target-nums[i]
            m[comp]=i