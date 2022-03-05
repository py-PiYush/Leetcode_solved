class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26,0,-1): 
            s = s.replace(str(i)+'#'*(i>9),chr(96+i))
        return s
        
        
        
        
        '''-----------'''
        mapp=dict(zip([str(i) if i<=9 else str(i)+'#' for i in range(1, 27)], list('abcdefghijklmnopqrstuvwxyz')))
        
        res=[]
        i=0
        while i<len(s):
            if i+2<len(s) and s[i+2]=='#':
                res.append(mapp[s[i:i+3]])
                i+=3
            else:
                res.append(mapp[s[i]])
                i+=1
        return ''.join(res)