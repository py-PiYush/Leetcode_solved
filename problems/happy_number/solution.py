class Solution:
    def isHappy(self, n: int) -> bool:
        def squareOfDigits(num):
            s = 0
            while num:
                s+=(num%10)**2
                num=num//10
            return s
        
        seen=set()
        while n!=1:
            n = squareOfDigits(n)
            if n in seen:
                return False
            seen.add(n)
        return True