class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        for i in range(len(intervals)):
            start,end=intervals[i]
            if not res or res[-1][1]<start:
                res.append([start,end])
            else:
                res[-1][1]=max(res[-1][1],end)
        return res