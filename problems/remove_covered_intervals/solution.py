class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : (x[0], -x[1]))
        max_=float('-inf')
        cnt=0
        for l, r in intervals:
            if max_ < r:
                cnt+=1
                max_=r
            
        return cnt