class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ''' Memoization'''
        @lru_cache(None)
        def recur(r, c, moves):
            if not (0<=r<m and 0<=c<n):
                return 1
            if moves==maxMove: return 0
            ans = 0
            for i in range(4):
                ans = (ans + recur(r+DIR[i], c+DIR[i+1], moves+1))%mod
            return ans
        
        mod = 1_000_000_007
        DIR = [0, 1, 0, -1, 0]
        return recur(startRow, startColumn, 0)
        
        
        ''' DFS (TLE)'''
        def dfs(r, c, moves):
            nonlocal cnt
            if not (0<=r<m and 0<=c<n):
                cnt+=1
                return
            if moves==maxMove:
                return
            dfs(r+1, c, moves+1)
            dfs(r, c+1, moves+1)
            dfs(r-1, c, moves+1)
            dfs(r, c-1, moves+1)
        
        cnt=0
        mod = 10**9 + 7
        dfs(startRow, startColumn, 0)
        return cnt%mod
            