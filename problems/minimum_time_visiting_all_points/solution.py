class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        lastX, lastY = points[0]
        count=0
        for i in range(1, len(points)):
            x,y=points[i][0], points[i][1]
            
            if x>lastX and y>lastY:
                while lastX<x and lastY<y:
                    count+=1
                    lastX+=1
                    lastY+=1
            elif x<lastX and y<lastY:
                while lastX>x and lastY>y:
                    count+=1
                    lastX-=1
                    lastY-=1
            elif x>lastX and y<lastY:
                while lastX<x and lastY>y:
                    count+=1
                    lastX+=1
                    lastY-=1
            else:
                while lastX>x and lastY<y:
                    count+=1
                    lastX-=1
                    lastY+=1
            count+=abs(x-lastX)+abs(y-lastY)
            lastX, lastY=x,y
        
        return count