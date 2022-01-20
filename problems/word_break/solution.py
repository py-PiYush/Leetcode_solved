class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ''' Bottom up '''
        n=len(s)
        dp=[False]*n
        
        for i in range(n):
            for word in wordDict:
                if i>=len(word)-1 and (i==len(word)-1 or dp[i-len(word)]):
                    if s[i-len(word)+1:i+1] == word:
                        dp[i]=True
                        break
        return dp[-1]
    
    
        ''' top down '''
        @lru_cache(None)
        def dp(i):
            if i<0:
                return True
            
            for word in wordDict:
                if i>=len(word)-1 and dp(i-len(word)):
                    if s[i-len(word)+1:i+1] == word:
                        return True
            return False
        
        return dp(len(s)-1)