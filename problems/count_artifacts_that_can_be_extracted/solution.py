class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        
        grid = [[-1]*n for _ in range(n)]
        atype = 1
        for r1, c1, r2, c2 in artifacts:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    grid[i][j] = atype
            atype+=1
        
        for r,c in dig:
            grid[r][c]='D'
            
        rem = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in rem:
                    rem.add(grid[i][j])
        
        g=len(rem)
        if -1 in rem:
            g-=1
        if 'D' in rem:
            g-=1
        return len(artifacts)-g