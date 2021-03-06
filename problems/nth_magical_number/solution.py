class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        a, b = A, B
        while b: a, b = b, a % b
        l, r, lcm = 2, 10**14, A * B // a
        while l < r:
            m = (l + r) // 2
            if m // A + m // B - m // lcm < N: l = m + 1
            else: r = m
        return l%(10**9 + 7)