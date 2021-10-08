from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        '''O(m+n)'''
#         countR=[0]*26
#         countM=[0]*26
        
#         for ch in ransomNote:
#             countR[ord(ch)-97]+=1
            
#         for ch in magazine:
#             countM[ord(ch)-97]+=1
     
#         for ch in ransomNote:
#             if countR[ord(ch)-97]>countM[ord(ch)-97]:
#                 return False
            
#         return True
    
        '''Using Counter'''
        return not Counter(ransomNote)-Counter(magazine)