class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        comp=sorted(heights)
        return sum([i!=j for i,j in zip(heights,comp)])