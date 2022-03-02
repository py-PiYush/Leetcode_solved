class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(count, queens, xy_diff, xy_sum):
            row=len(queens)
            
            for col in range(n):
                if not col in queens and not row - col in xy_diff and not row+col in xy_sum:
                    if row+1==n:
                        count+=1
                    else:
                        count = dfs(count, queens+[col], xy_diff + [row-col], xy_sum + [row+col])
            return count
        return dfs(0,[],[],[])
        
        