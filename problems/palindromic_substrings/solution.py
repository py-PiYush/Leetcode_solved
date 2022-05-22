class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        def getDP(left, right):
            if left > right: return True
            return dp[left][right]

        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    dp[i][j] = getDP(i + 1, j - 1)
                if dp[i][j]:
                    ans += 1
        return ans