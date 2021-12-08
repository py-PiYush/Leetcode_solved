class Solution:
    def titleToNumber(self, s: str) -> int:
        
        
        '''converting base26 to base10'''
        s = s[::-1]
        sum = 0
        for exp, char in enumerate(s):
            sum += (ord(char) - 65 + 1) * (26 ** exp)
        return sum
    
    
    
    
    
        
        ttonum=dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),range(1,27)))
        #print(ttonum)
        num=0
        times=0
        for i in s[::-1]:
            num+=(26**times)*ttonum[i]
            times+=1
        return num