from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        '''Two pointer'''
#         n1,n2,result=sorted(nums1),sorted(nums2), []
#         p1=p2=0
        
#         while p1<len(n1) and p2<len(n2):
#             if n1[p1]<n2[p2]:
#                 p1+=1
#             elif n1[p1]>n2[p2]:
#                 p2+=1
#             else:
#                 result.append(n1[p1])
#                 p1+=1
#                 p2+=1
#         return result
    
        '''Using collections.Counter'''
        # result=[]
        # c1,c2 = Counter(nums1), Counter(nums2)
        # for i in c1:
        #     if i in c2:
        #         result+=[i]*min(c1[i],c2[i])
        # return result
        
        return (Counter(nums1) & Counter(nums2)).elements()