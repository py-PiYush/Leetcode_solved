from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        '''Non-Optimal'''
#         def isPermutation(s1,s2):
#             return Counter(s1)==Counter(s2)
        
#         if len(s2)<len(s1):
#             return False
        
#         start,end=0,len(s1)-1
#         while end<len(s2):
#             subStr=s2[start:end+1]
#             if isPermutation(s1,subStr):
#                 return True
#             start+=1
#             end+=1
            
#         return False

        '''No need to use Counter again and again'''
#         count1=Counter(s1)
#         count2=Counter(s2[:len(s1)])
        
#         start,end=0,len(s1)
#         while end < len(s2):
#             if count1==count2: return True
#             count2[s2[start]]-=1
#             if count2[s2[start]]<1:
#                 count2.pop(s2[start])
#             count2[s2[end]]=count2.get(s2[end],0)+1
#             start+=1
#             end+=1
#         return count1==count2

        '''Default dict is faster than counter'''
        count1=defaultdict(int)
        count2=defaultdict(int)
        for x in s1: count1[x]+=1
        for x in s2[:len(s1)]: count2[x]+=1
            
        start,end=0,len(s1)
        while end < len(s2):
            if count1==count2: return True
            count2[s2[start]]-=1
            if count2[s2[start]]<1:
                count2.pop(s2[start])
            count2[s2[end]]+=1
            start+=1
            end+=1
        return count1==count2
        