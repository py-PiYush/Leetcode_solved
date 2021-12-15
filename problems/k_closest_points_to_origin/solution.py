class Solution:
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2
    
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''<------------QuickSelect---------------->'''
        
        def partition(points, left, right):
            pivot=points[left + (right-left)//2]
            pivot_dist=self.squared_distance(pivot)
            while left < right:
                if self.squared_distance(points[left])>=pivot_dist:
                    points[left], points[right]=points[right], points[left]
                    right-=1
                else:
                    left+=1
            if self.squared_distance(points[left])< pivot_dist:
                left+=1
            return left
        
        left, right=0, len(points)-1
        pIdx=len(points)
        while pIdx!=k:
            pIdx=partition(points, left, right)
            if pIdx<k:
                left=pIdx
            else:
                right=pIdx -1
        return points[:k]
        
        
        
        '''<-------------Binary Search------------->'''
#         def split_distances(rem,distances, mid):
#             closer, farther=[],[]
#             for i in rem:
#                 if distances[i]<=mid:
#                     closer.append(i)
#                 else:
#                     farther.append(i)
#             return closer, farther
        
#         distances=list(map(lambda x: sqrt(x[0]**2 + x[1]**2), points))
#         rem=[i for i in range(len(points))]
#         closest=[]
#         low, high = min(distances), max(distances)
#         while k:
#             mid=low + (high - low)/2
#             closer, farther = split_distances(rem, distances, mid)
#             if len(closer)>k:
#                 rem=closer
#                 high=mid
#             else:
#                 k-=len(closer)
#                 rem=farther
#                 closest.extend(closer)
#                 low=mid
#         return [points[i] for i in closest]
        
        
        
        '''<-----------------Using heap--------->'''
#         heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
#         heapq.heapify(heap)
#         for i in range(k, len(points)):
#             dist = -self.squared_distance(points[i])
#             if dist > heap[0][0]:
#                 heapq.heappushpop(heap, (dist, i))
#         return [points[i] for (_, i) in heap]
    
    
    
        '''<----------Using list sort----------->`'''
#         points.sort(key=lambda x: x[0]**2 + x[1]**2)
#         return points[:k]
            
    
    
        
        
        