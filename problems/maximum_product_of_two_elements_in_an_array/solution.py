class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        '''Using heap'''
        import heapq
        prod=1
        for i in heapq.nlargest(2,nums):
            prod*=(i-1)
        return prod
    
    
        '''Linear scan'''
        a=b=0
        for n in nums:
            if n>a:
                b=a
                a=n
            elif n>b:
                b=n
        return (a-1)*(b-1)
                