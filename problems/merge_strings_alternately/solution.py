class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a+b for a, b in zip_longest(word1, word2, fillvalue=''))        
        
        
        
        
        '''------------'''
        p1=0
        new=''
        while p1<len(word1) and p1<len(word2):
            new+=word1[p1]+word2[p1]
            p1+=1
        new+=word1[p1:]+word2[p1:]
        return new