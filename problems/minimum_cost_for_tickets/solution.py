class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i):
            
            #base case
            if i>365:
                return 0
            
            #travelling on a day
            elif i in dayset:
                return min(dp(i+d) + c for c, d in zip(costs, [1, 7, 30]))
            
            #not travelling
            else:
                return dp(i+1)
        
        dayset=set(days)
        return dp(days[0])