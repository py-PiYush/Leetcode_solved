class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        '''Using python library'''
        from itertools import combinations
        return combinations([i for i in range(1,n+1)], k)