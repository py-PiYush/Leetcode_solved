class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        count, end=0,-float('inf')
        for interval in points:
            if interval[0]>end:
                count+=1
                end=interval[1]
        return count