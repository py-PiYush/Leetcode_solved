class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ''' math '''
        p = max(0, (26*n - k - 1)//25)
        q = k - 26*n + 25*p + 26
        return "a"*p + chr(96 + q) + "z"*(n-p-1)
        
        
        ''' Greedy '''
        ans=['a']*n
        k-=n
        while k>0:
            n-=1
            ans[n]=chr(ord('a') + min(25, k))
            k-=min(25, k)
        return ''.join(ans)