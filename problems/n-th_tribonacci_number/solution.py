class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(i):
            if i not in memo:
                memo[i]=dp(i-1)+dp(i-2)+dp(i-3)
            return memo[i]
        memo={0:0, 1:1, 2:1}
        return dp(n)