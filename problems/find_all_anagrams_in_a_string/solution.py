class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        count_s=Counter(s[:len(p)-1])
        count_p=Counter(p)
        l, r = 0, len(p)-1
        res=[]
        while r<len(s):
            count_s[s[r]]+=1
            if count_s==count_p:
                res.append(l)
            count_s[s[l]]-=1
            l+=1
            r+=1
            
        return res
        
        
        
        
        ''' TLE '''
        def isAnagram(s1, s2):
            return Counter(s1)==Counter(s2)
        
        l, r = 0, len(p)-1
        res=[]
        while r<len(s):
            if isAnagram(s[l:r+1], p):
                res.append(l)
            l+=1
            r+=1
        
        return res
            