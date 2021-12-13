class Solution:
    def maxPower(self, s: str) -> int:
        cur,maxLength=0,0
        curChar=s[0]
        for i in range(len(s)):
            if s[i]!=curChar:
                curChar=s[i]
                cur=0
            cur+=1
            maxLength=max(maxLength, cur)
        return maxLength