class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        arr=[(abs(n[0]-x)+abs(n[1]-y), i) for i,n in enumerate(points) if n[0]==x or n[1]==y]
        print(arr)
        if not arr: return -1
        return sorted(arr, key=lambda x:(x[0], x[1]))[0][1]