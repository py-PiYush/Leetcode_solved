class Solution:
    def fib(self, n: int) -> int:
        
        
        '''iterative'''
        if n==0 or n==1:
            return n
        a,b=0,1
        for _ in range(n):
            a,b=b,b+a
        return a
        
        '''recursive'''
#         def recurse(n):
#             if n in cache:
#                 return cache[n]
#             result = recurse(n-1)+recurse(n-2)
#             cache[n]=result
#             return result
        
#         cache={0:0, 1:1}
#         return recurse(n)

        '''tail recursion'''
        def rec(n,a=0,b=1):
            if n==0:
                return a
            if n==1:
                return b
            return rec(n-1,b,a+b)
        return rec(n)