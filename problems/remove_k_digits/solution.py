class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                k -= 1
                stack.pop()  
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]     
        return "".join(stack).lstrip("0") or "0"
        
        
        
        
        '''Recursion (TLE)'''
        def helper(s, k):
            if k==0:
                return s
            minimum='9'*(10**5)
            for i in range(len(s)):
                n=s[:i]+s[i+1:]
                if int(n)<int(minimum):
                    minimum=n
            return helper(minimum, k-1)
        
        if k>=len(num): return '0'
        ans=helper(num,k)
        if ans[0]=='0': return str(int(ans)) 
        return ans