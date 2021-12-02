class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rob(i):
            return max(rob(i+1), nums[i] + rob(i+2)) if i < len(nums) else 0
        return rob(0)