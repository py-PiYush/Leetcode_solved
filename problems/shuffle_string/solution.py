class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        ''' O(n) time and space'''
        res=[0]*len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
            
        return ''.join(res)
        
        ''' Sorting '''
        return ''.join([x[1] for x in sorted(list(zip(indices, list(s))))])
    
    
        '''Cyclic Sort'''
        s = list(s)
        cur = 0
        while cur < len(s):
            if cur == indices[cur]:
                cur += 1
                continue
            newIndex = indices[cur]
            s[cur], indices[cur], s[newIndex], indices[newIndex] = s[newIndex], indices[newIndex] , s[cur], indices[cur]
        return "".join(s)
                