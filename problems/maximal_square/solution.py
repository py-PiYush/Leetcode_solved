class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        '''Brute Force'''
        if not matrix: return
        rows, cols=len(matrix), len(matrix[0])
        maxSq=0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='1':
                    sq=1
                    flag=True
                    while sq+i<rows and sq+j<cols and flag:
                        for k in range(j, sq+j+1):
                            if matrix[i+sq][k]=='0':
                                flag=False
                                break
                        for k in range(i, sq+i+1):
                            if matrix[k][j+sq]=='0':
                                flag=False
                                break
                        if flag:
                            sq+=1
                        
                    maxSq=max(maxSq, sq)
        return maxSq**2