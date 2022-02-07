class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''Xor'''
        code = 0
        for ch in s:
            code ^= ord(ch)
        for ch in t:
            code ^= ord(ch)
        return chr(code)
        
        
        ''' Counter '''
        return [i for i in (Counter(t)-Counter(s)).keys()][0]