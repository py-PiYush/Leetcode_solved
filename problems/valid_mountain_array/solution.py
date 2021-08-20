class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
            
        pivot=len(arr)
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                pivot=i
                break
        print(pivot)
        
        if pivot == len(arr) or pivot == 0:
            return False
        
        for i in range(pivot-1):
            if arr[i]>arr[i+1]:
                return False
            
        for j in range(pivot,len(arr)-1):
            if arr[j]<arr[j+1]:
                return False
            
        return True
    
                
        
#         N = len(A)
#         i = 0

#         # walk up
#         while i+1 < N and A[i] < A[i+1]:
#             i += 1

#         # peak can't be first or last
#         if i == 0 or i == N-1:
#             return False

#         # walk down
#         while i+1 < N and A[i] > A[i+1]:
#             i += 1

#         return i == N-1