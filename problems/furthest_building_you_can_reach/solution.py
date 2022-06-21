class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ''' min heap '''
        heap = []
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff>0:
                heapq.heappush(heap, diff)
            if len(heap)>ladders:
                bricks -= heapq.heappop(heap)
            if bricks<0:
                return i
        return len(heights)-1
        
        
        ''' Binary Search '''
        def condition(k):
            to_climb = []
            for i in range(1,k+1):
                if heights[i]-heights[i-1]>0:
                    to_climb.append(heights[i]-heights[i-1])
            
            return len(to_climb)<=ladders or sum(sorted(to_climb, reverse=True)[ladders:]) <=bricks
        
        heights.append(float('inf'))
        left, right = 0, len(heights)-1
        while left<right:
            mid = left + (right - left)//2
            if condition(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1