class Solution:
    def climbStairs(self, n: int) -> int:
        def fibonacci(n):
            if n==0 or n==1:
                return n
            a,b=0,1
            for _ in range(n):
                a,b=b,b+a
            return a
        return fibonacci(n+1)