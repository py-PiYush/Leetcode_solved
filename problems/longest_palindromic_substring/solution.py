class Solution:
    def longestPalindrome(self, s: str) -> str:
        def createPalin(s, l, r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        res=''
        for i in range(len(s)):
            #odd case
            tmp = createPalin(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            
            #even case
            tmp = createPalin(s, i, i+1)
            if len(tmp)>len(res):
                res = tmp
        return res