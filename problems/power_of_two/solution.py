class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        return n>0 and n&(n-1)==0
    
        '''recursive'''
        if n==1: return True
        if n<1: return False
        return self.isPowerOfTwo(n/2)