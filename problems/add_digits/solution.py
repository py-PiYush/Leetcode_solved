class Solution:
    def addDigits(self, num: int) -> int:
        '''
        Math solution 
        dr(n)=0,if n=0
        dr(n)=9,if n=9k
        else,
        dr(n)=nmod9
        '''
        if num == 0 : return 0
        if num%9 == 0 : return 9
        return num%9
        
        
        
        '''-----------------'''
        result=0
        while  num:
            result+=(num%10)
            num//=10
            if num==0 and result>9:
                num=result
                result=0
        return result