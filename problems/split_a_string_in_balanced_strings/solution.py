class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal=0
        ans=0
        for i in s:
            if i=='R':
                bal-=1
            elif i=='L':
                bal+=1
            if bal==0:
                ans+=1
        return ans
        