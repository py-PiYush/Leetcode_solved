class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, ans = [], [-1]*len(nums)
        for i, n in enumerate(nums+nums):
            while stack and nums[stack[-1]]<n:
                ans[stack.pop()] = n
            stack.append(i%len(nums))
        return ans