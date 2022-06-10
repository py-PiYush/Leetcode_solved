class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        c={}
        for l1,l2 in zip(s,t):
            if l1 in d and d[l1]!=l2:
                return False
            else:
                d[l1]=l2
            if l2 in c and c[l2]!=l1:
                return False
            else:
                c[l2]=l1
            
        print(d, c, sep='\n')
        return True
            