class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        m = len(set(candyType))
        return m if m<=n//2 else n//2