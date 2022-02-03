class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        
        n=len(grid)
        dirs=[(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1, -1), (-1, 1)]
        queue=deque([(0,0,1)])
        seen=set((0,0))
        
        while queue:
            cur_row, cur_col, ans = queue.popleft()
            if cur_row==cur_col==n-1:
                return ans

            for dx, dy in dirs:
                nr, nc=cur_row + dx, cur_col + dy
                if (
                    nr<0 or nr==n or
                    nc<0 or nc==n or
                    grid[nr][nc]==1 or (nr, nc) in seen
                ):
                    continue
                queue.append((nr, nc, ans+1))
                seen.add((nr, nc))
        
        return -1
                    
