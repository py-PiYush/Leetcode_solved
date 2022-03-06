class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)
        
        if nums[n - 1] <= k + n:
            return (k + n) * (k + n + 1) // 2 - sum(nums)

        lft, rgt = 0, n - 1
        while rgt > lft:
            mid = (lft + rgt) // 2
            if nums[mid] - mid <= k:
                lft = mid + 1
            else:
                rgt = mid

        return (k + lft) * (k + lft + 1) // 2 - sum(nums[:lft])