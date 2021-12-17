class Solution:
    
    
    def __init__(self):
        self.dic = {1:1, 2:2}
    
    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]
    
    
    
    
    # def climbStairs(self, n: int) -> int:
    #     def fibonacci(n):
    #         if n==0 or n==1:
    #             return n
    #         a,b=0,1
    #         for _ in range(n):
    #             a,b=b,b+a
    #         return a
    #     return fibonacci(n+1)