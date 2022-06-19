class Solution:
    def greatestLetter(self, s: str) -> str:
        
        ''' Using hashmap'''
        d, ans = defaultdict(set), ''
        for c in s:
            uc = c.upper()
            d[uc].add(c)
            if len(d[uc]) == 2:
                ans = max(ans, uc)
        return ans
        
        
        ''' Brute Force'''
        ans=''
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i].islower() and s[j].isupper() and s[i]==s[j].lower() and s[j]>ans:
                    ans = s[j]
                elif s[i].isupper() and s[j].islower() and s[j] == s[i].lower() and s[i]>ans:
                    ans = s[i]
        return ans
                    