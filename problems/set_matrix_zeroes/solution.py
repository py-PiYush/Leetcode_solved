class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''O(1) space'''
        m,n=len(matrix[0]), len(matrix)
        r1=any(matrix[0][j]==0 for j in range(m))
        c1=any(matrix[i][0]==0 for i in range(n))
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[0][j]*matrix[i][0]==0:
                    matrix[i][j]=0
        
        if r1:
            for j in range(m):
                matrix[0][j]=0
        if c1:
            for i in range(n):
                matrix[i][0]=0
        
        
        '''O(m+n) space'''
        # row,col=set(),set()
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==0:
        #             row.add(i)
        #             col.add(j)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if i in row or j in col:
        #             matrix[i][j]=0
                    