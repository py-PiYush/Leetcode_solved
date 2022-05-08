class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        
        """
        n = len(arr)
        cntZero = arr.count(0)
        newLen = n + cntZero # Length of new array if we don't trim up to length `n`
        
        # Let's copy values from the end
        i = n - 1
        j = newLen - 1
        while j >= 0:
            if j < n: arr[j] = arr[i]
            j -= 1
            if arr[i] == 0: # Copy twice if arr[i] == 0
                if j < n: arr[j] = arr[i]
                j -= 1
            i -= 1
        
        '''--------------------------------'''
        
#         def shift(i):
#             for j in range(len(arr)-1, i, -1):
#                 arr[j]=arr[j-1]
#             arr[i+1]=0
            
            
#         last=len(arr)-1
#         i=last-1
#         while i>=0:
#             if arr[i]==0:
#                 shift(i)
#             i-=1
        
        '''------------------'''
        
#         n=len(arr)
#         i=0
#         while i<n:
#             if arr[i]==0:
#                 arr.insert(i,0)
#                 i+=2
#             else:
#                 i+=1
#         while len(arr)>n:
#             arr.pop()
        
                
        