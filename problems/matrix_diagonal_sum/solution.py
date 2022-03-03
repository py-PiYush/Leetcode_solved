class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        n=len(mat)
        r,c=0,0
        while r<n and c<n:
            summ+=mat[r][c]
            if r!=n-c-1:
                summ+=mat[r][n-c-1]
            r+=1
            c+=1
            
        return summ