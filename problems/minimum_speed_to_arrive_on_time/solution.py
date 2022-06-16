class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def condition(k):
            total=0
            for i in range(len(dist)-1):
                total += (dist[i]-1)//k + 1
            total += dist[-1]/k
            return total<=hour
        
        if len(dist) - 1>=hour: return -1
        left, right = 1, max(dist)*100
        while left<right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid+1
        return left