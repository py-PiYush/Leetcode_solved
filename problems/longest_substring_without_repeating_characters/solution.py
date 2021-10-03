class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         l,r=0,0
#         len_=0
#         set_=set()
#         while r<len(s):
            
#             if s[r] not in set_:
#                 set_.add(s[r])
#                 if r-l+1 >len_:
#                     len_=r-l+1
#                 r+=1
#             else:
#                 while s[r] in set_:
#                     set_.remove(s[l])
#                     l+=1
            
#         return len_

        start=maxLength=0
        used={}
        for i,char in enumerate(s):
            if char in used and start<=used[char]:
                start=used[char]+1
            else:
                maxLength=max(maxLength, i-start+1)
            
            used[char]=i
        return maxLength
        
            