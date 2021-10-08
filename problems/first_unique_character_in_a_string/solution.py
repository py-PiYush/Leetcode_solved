from collections import Counter
import string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
#         '''O(n^2)''' # TLE
#         for i in range(len(s)):
#             flag=True
#             for j in range(len(s)):
#                 if s[i]==s[j] and i!=j:
#                     flag=False
#             if flag:
#                 return i
            
#         return -1


#         '''O(n)'''
#         count=dict()
#         for i,letter in enumerate(s):
#             if letter in count:
#                 count[letter]=(i,-1)
#             else:
#                 count[letter]=(i,1)
        
#         print(count)
#         result=[i for i,cnt in count.values() if cnt==1]
#         if len(result)==0:
#             return -1
#         return min(result)
    
    
        
    
        '''Better version'''
#         counts=[0]*26
#         for ch in s:
#             counts[ord(ch)-97]+=1
        
#         for i,ch in enumerate(s):
#             if counts[ord(ch)-97]==1:
#                 return i
#         return -1
    
        '''Faster'''
        # Faster because bultin string functions in python are written in C
        return min((s.index(char) for char in string.ascii_lowercase if s.count(char)==1), default=-1)