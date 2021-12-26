class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
#         def valid(row,col, res):
#             if row in res:
#                 return False
#             i,j,k,l=row-1,col-1,row+1,col-1
#             while i>=0 and j>=0:
#                 if res[j]==i:
#                     return False
#                 i-=1
#                 j-=1
#             while k<n and l>=0:
#                 if res[l]==k:
#                     return False
#                 k+=1
#                 l-=1
#             return True
        
#         def solve(col, res, ans):
#             # print(res, col, ans)
#             if col==n :
#                 ans.append(res[:])
#                 res=[-1]*n
#                 return
#             for i in range(n):
#                 if valid(i,col, res):
#                     res[col]=i
#                     solve(col+1, res, ans)
#                     res[col]=-1
        
#         res=[-1]*n
#         ans=[]
#         solve(0, res, ans)
#         board=[['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in ans]
#         return board   
        
        
        '''A better sol'''
        def DFS(valid_configs, queens, yx_diffs, yx_sums):
            """`valid_configs` contains configurations of n queens that satisfy
            threat constraints.

            Each element in `queens` represents the position of a queen.
            Its row is indicated by the element *index* and its column is
            indicated by the element *value*. Given this, duplicate values
            in `queens` would mean two rows had a queen in the same column,
            which isn't allowed.
            
            yx_diffs and yx_sums both represent diagonals that are threatened
            by a queen in `queens`. As shown below, diagonals can be represented
            with a single integer calculated from the difference or sum of a
            position's row and columns indices. Differences (row - col) are
            left->right diagonals and sums are right->left diagonals.
            
            yx_diffs (row_idx - col_idx):
            3 |  3  2  1  0
            2 |  2  1  0 -1
            1 |  1  0 -1 -2
            0 |  0 -1 -2 -3
            r  ------------
              c  0  1  2  3

            yx_sums (row_idx + col_idx):
            3 |  3  4  5  6
            2 |  2  3  4  5
            1 |  1  2  3  4
            0 |  0  1  2  3
            r  ------------
              c  0  1  2  3
            """
            row_idx = len(queens)
            
            if row_idx == n:
                valid_configs.append(queens)
                return
            
            for col_idx in range(n):
                if not col_idx in queens and not row_idx - col_idx in yx_diffs and not row_idx + col_idx in yx_sums:
                    DFS(valid_configs, queens + [col_idx], yx_diffs + [row_idx-col_idx], yx_sums + [row_idx + col_idx])
        
        result = []
        DFS(result, [],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]