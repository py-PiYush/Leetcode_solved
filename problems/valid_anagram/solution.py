from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''using sort'''
        # return sorted(s)==sorted(t)
    
        '''using Counter'''
        # return not Counter(s)-Counter(t) if len(s)==len(t) else False
        
        '''Dictionary'''
        count={}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        
        for j in t:
            if j not in count:
                return False
            count[j]-=1
            
        for value in count.values():
            if value!=0:
                return False
        
        return True