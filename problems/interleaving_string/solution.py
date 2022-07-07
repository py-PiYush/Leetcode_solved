class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ''' DFS '''
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        stack, visited = [(0, 0)], set((0, 0))
        while stack:
            x, y = stack.pop()
            if x+y == l:
                return True
            if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1, y)); visited.add((x+1, y))
            if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                stack.append((x, y+1)); visited.add((x, y+1))
        return False
        
        
        ''' Recursion + memo (MLE)'''
        @lru_cache(None)
        def is_interleave(i,j,res):
            if res==s3 and i==len(s1) and j==len(s2):
                return True
            ans = False
            if i<len(s1):
                ans |= is_interleave(i+1, j, res+s1[i])
            if j<len(s2):
                ans |= is_interleave(i, j+1, res+s2[j])
            return ans
        
        if len(s1)+len(s2) != len(s3):
            return False
        return is_interleave(0,0,'')
    
        