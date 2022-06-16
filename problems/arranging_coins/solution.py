class Solution:
    def arrangeCoins(self, n: int) -> int:
        def condition(k):
            return k*(k+1)//2 > n
        left, right = 0, n+1
        while left < right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1