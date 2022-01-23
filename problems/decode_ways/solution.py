class Solution:
    def numDecodings(self, s: str) -> int:
        #edge cases
        if not s or s[0]=='0':
            return 0
            
        dp=[1]*len(s)
        
        for i in range(1, len(s)):
            #one digit check
            dp[i]=0 if int(s[i])==0 else dp[i-1]
            
            #two digit check
            if 10<= int(s[i-1:i+1]) <= 26:
                dp[i]+= dp[i-2 if i>1 else 0]
        return dp[-1]