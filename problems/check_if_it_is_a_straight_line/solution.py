class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True
        
        
        
        '''----------------'''
        slope=set()
        for i in range(1, len(coordinates)):
            x1, y1 = coordinates[i-1]
            x2, y2 = coordinates[i]
            slope.add((y2-y1)/(x2-x1) if x2-x1!=0 else float('inf'))
        return len(slope)==1