class Solution:
    def reverse(self, x: int) -> int:
        
        s=str(abs(x)).rstrip('0')
        if s=='':
            return x
        
        num=int(s[::-1])
        if x<0:
            num*=-1
        if -2**31<=num<=2**31-1:
            return num
        else:
            return 0
        