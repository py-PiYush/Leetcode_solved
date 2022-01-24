class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        
        for row in range(1, n):
            for col in range(n):
                sumUpLeft = matrix[row-1][col-1] if col>0 else float('inf')
                sumUpRight = matrix[row-1][col+1] if col<n-1 else float('inf')
                matrix[row][col]+=min(sumUpLeft, sumUpRight, matrix[row-1][col])
        
        # print(matrix)
        return min(matrix[-1])