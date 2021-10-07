class Solution:
    def reverseWords(self, s: str) -> str:
        
#         def reverse(word):
#             lst=list(word)
#             for i in range(len(lst)//2):
#                 lst[i],lst[-i-1]=lst[-i-1],lst[i]
#             return ''.join(lst)
        
#         lst=s.split(' ')
#         print(lst)
      
#         for i in range(len(lst)):
#             lst[i]=reverse(lst[i])
#         s=' '.join(lst)
#         return s

        '''Without using split'''
        s=list(s)
        start=0
        while start<len(s):
            end=start
            while end+1<len(s) and s[end+1]!=' ':
                end+=1
            nextWord=end+2
            
            while start<end:
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1
            start=nextWord
        return ''.join(s)
            
        
        