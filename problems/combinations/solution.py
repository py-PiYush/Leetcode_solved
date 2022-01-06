class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        '''Using python library'''
        from itertools import combinations
        return combinations([i for i in range(1,n+1)], k)
        
        '''Recursion'''
        # if k == 0:
        #     return [[]]
        # return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
    
        '''Backtracking'''
        def backtrack(first=0, cur=[]):
            if len(cur)==k:
                ans.append(cur[:])
                return
            
            for i in range(first, n):
                backtrack(i+1, cur+[nums[i]])
        
        ans=[]
        nums=list(range(1,n+1))
        backtrack()
        return ans