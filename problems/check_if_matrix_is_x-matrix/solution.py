class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][i]==0 or grid[i][-1-i]==0:
                    # print('first condition false at', i)
                    return False
                if i!=j and i+j!=len(grid)-1  and grid[i][j]!=0:
                    # print('second condition false at', (i,j))
                    return False
        return True