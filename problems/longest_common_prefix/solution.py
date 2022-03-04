class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        '''based on shortest string'''
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
        
        
        
        ''' Lcp of every consecutive strings'''
        def lcp(s1, s2):
            i, j =0, 0
            pref=[]
            while i<len(s1) and j<len(s2):
                if s1[i]==s2[j]:
                    pref.append(s1[i])
                    i+=1
                    j+=1
                else:
                    break
            return ''.join(pref)
        
        for i in range(len(strs)-1):
            strs[i+1]=lcp(strs[i], strs[i+1])
        return strs[-1]