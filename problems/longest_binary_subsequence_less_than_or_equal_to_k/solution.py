class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        i = 0
        while int(s[-i-1:], 2) <= k and i < 32 and i < len(s):
            i += 1
        return s[:-i].count('0') + i
        
        '''Recursion'''
        self.max = 0
        @lru_cache()
        def f(i, res):
            if res and int(res, 2) <=k:
                self.max = max(self.max, len(res))
            if i == len(s):
                return
            f(i+1, res+s[i])
            f(i+1, res)
        
        f(0,'')
        return self.max