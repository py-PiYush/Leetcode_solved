class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice, maxProfit = float('inf'), 0
        for n in prices:
            if minPrice>n:
                minPrice=n
                continue
            maxProfit=max(maxProfit, n-minPrice)
        
        return maxProfit
            