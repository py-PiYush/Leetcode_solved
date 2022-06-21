class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        '''s+s contains goal, O(n^2)'''
        return len(s)==len(goal) and goal in s+s
        
        
        ''' Brute Force, check for every rotation, O(n^2)'''
        if len(s)!=len(goal): return False
        for i in range(len(s)):
            new = s[i:] + s[:i]
            if new == goal:
                return True
        return False