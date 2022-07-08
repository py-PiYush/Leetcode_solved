class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def recur(idx, n_cnt, prev_color):
            if idx == len(houses):
                return (max_cost,0)[n_cnt==target]
            if n_cnt>target:
                return max_cost
            
            min_cost = max_cost
            if houses[idx]!=0:
                min_cost = recur(idx+1, n_cnt + (prev_color!=houses[idx]), houses[idx])
            else:
                for color in range(1, len(cost[0])+1):
                    cur = cost[idx][color-1] + recur(idx+1, n_cnt + (prev_color!=color), color)
                    min_cost = min(min_cost, cur)
            return min_cost
        
        max_cost = float('inf')
        ans = recur(0, 0, 0)
        return ans if ans!=max_cost else -1