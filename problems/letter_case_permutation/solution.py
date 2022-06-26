class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def recur(idx, res):
            if idx==len(s):
                ans.append( res)
                return
            if s[idx].isalpha():
                recur(idx+1,res+s[idx].upper())
                recur(idx+1, res+s[idx].lower())
            else:
                recur(idx+1,res+s[idx] )
        ans = []
        recur(0,'')
        return ans
        
        res = ['']
        for ch in s:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res