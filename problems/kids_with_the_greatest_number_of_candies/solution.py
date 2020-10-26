class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_=max(candies)
        res=[i+extraCandies>=max_ for i in candies]
        return res
        
        