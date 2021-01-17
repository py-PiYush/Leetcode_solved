class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        cnt=0
        while(n):
            cnt+=1
            n=n&(n-1)
        return cnt==1