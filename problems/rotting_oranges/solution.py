class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting: return -1
            rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
            fresh -= rotting
            timer += 1
        return timer
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        rows,cols=len(grid), len(grid[0])
        rotten=deque([])
        fresh_count=0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    rotten.append((r,c))
                if grid[r][c]==1:
                    fresh_count+=1
        
        print(rotten, fresh_count)
        minutes=0
        while rotten and fresh_count>0:
            minutes+=1
            for _ in range(len(rotten)):
                r,c=rotten.popleft()
                for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nr, nc=r+dx, c+dy
                    if nr<0 or nr==rows or nc<0 or nc==cols or grid[nr][nc]==0 or grid[nr][nc]==2:
                        continue

                    fresh_count-=1
                    grid[nr][nc]=2
                    rotten.append((nr,nc))
                    
        return minutes if fresh_count==0 else -1
            