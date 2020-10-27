class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i=0
        res=0
        while i<n:
            num=start+2*i
            res^=num
            i+=1
        return res