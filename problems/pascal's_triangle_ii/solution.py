class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''Recursive'''
#         memo={}
#         def getElement(i,j):
#             if j==0 or j==i:
#                 return 1
#             if (i,j) in memo:
#                 return memo[(i,j)]
            
#             n=getElement(i-1,j-1)+getElement(i-1,j)
#             memo[(i,j)]=n
#             return n
        
#         res=[getElement(rowIndex,j) for j in range(rowIndex+1)]
#         return res
    
        '''Iterative'''
        row=[1]
        for _ in range(rowIndex):
            row=[x+y for x,y in zip([0]+row, row+[0])]
        return row