class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0,0
        if not s: return True
        if len(s)>len(t): return False
        
        while i < len(s) and j < len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1

        return i==len(s)