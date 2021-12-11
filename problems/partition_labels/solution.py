class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        '''Greedy'''
#         last={c:i for i,c in enumerate(s)}
#         j=anchor=0
#         ans=[]
#         for i,c in enumerate(s):
#             j=max(j,last[c])
#             if i==j:
#                 ans.append(i-anchor+1)
#                 anchor=i+1
#         return ans
    
        '''Merge intervals'''
        def mergeIntervals(intervals):
            intervals.sort(key=lambda x:x[0])
            merged=[]
            for i in range(len(intervals)):
                start, end=intervals[i]
                if not merged or merged[-1][1]<start:
                    merged.append([start, end])
                else:
                    merged[-1][1]=max(merged[-1][1], end)
            return merged
        
        intervals=[]
        ans=[]
        for i in set(s):
            beg=s.index(i)
            end=s.rindex(i)
            intervals.append([beg,end])
        merged=mergeIntervals(intervals)
        for i in merged:
            ans.append(i[1]-i[0]+1)
        return ans