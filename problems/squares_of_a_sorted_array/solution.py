class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        '''Approach 1'''
        # return sorted([i**2 for i in A])
        
        '''Approach 2'''
#         pos=self.first_non_negative(A)
#         neg=pos-1
#         res=[]
        
#         print(pos,neg)
        
#         while pos<len(A) and neg>=0:
#             if A[pos]**2 <= A[neg]**2:
#                 res.append(A[pos]**2)
#                 pos+=1
#             else:
#                 res.append(A[neg]**2)
#                 neg-=1
                
#         if pos>=len(A) and neg>=0:
#             res+=[i**2 for i in A[neg::-1]]
#         if neg<0 and pos<len(A):
#             res+=[i**2 for i in A[pos:]]
#         return res
    
#     def first_non_negative(self,A):
#         for i in range(len(A)):
#             if A[i]>=0:
#                 return i
#         return len(A)
        
    
        '''Approach 3'''
        l,r=0,len(A)-1
        res=[]
        while r>=l:
            if A[r]**2>=A[l]**2:
                res.append(A[r]**2)
                r-=1
            else:
                res.append(A[l]**2)
                l+=1
        return reversed(res)