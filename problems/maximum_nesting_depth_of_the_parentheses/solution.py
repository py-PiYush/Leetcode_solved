class Solution:
    def maxDepth(self, s: str) -> int:
        cnt=0
        max_=0
        for i in s:
            if i=='(':
                cnt+=1
            max_=max(max_,cnt)
            if i==')':
                cnt-=1
        return max_
        