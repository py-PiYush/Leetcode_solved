class UnionFind:
    def __init__(self, size):
        self.root=[i for i in range(size)]
        self.rank=[1]*size
    
    def find(self, x):
        if self.root[x]==x:
            return x
        self.root[x]=self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
class Edge:
    def __init__(self, start, end, cost):
        self.point1=start
        self.point2=end
        self.cost=cost
    
    def __lt__(self, other):
        return self.cost < other.cost

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''--------- Prim's Algo ---------------'''
        if not points:
            return 0
        
        n=len(points)
        pq=[]
        visited=[False]*n
        result=0
        count=n-1
        
        x1, y1 = points[0]
        for j in range(1,n):
            x2, y2=points[j]
            cost = abs(x2-x1) + abs(y2 - y1)
            edge=Edge(0, j, cost)
            pq.append(edge)
        visited[0]=True
        
        heapq.heapify(pq)
        
        while pq and count>0:
            edge=heapq.heappop(pq)
            point1 = edge.point1
            point2 = edge.point2
            cost = edge.cost
            if not visited[point2]:
                result+=cost
                visited[point2]=True
                for j in range(n):
                    if not visited[j]:
                        dist = abs(points[point2][0] - points[j][0])+\
                        abs(points[point2][1] - points[j][1])
                        heapq.heappush(pq,Edge(point2, j, dist))
                count-=1
        
        return result
            
            
        
        
        '''--------- Kruskal's Algo ------------'''
        if not points:
            return 0
        
        n=len(points)
        pq=[]
        uf=UnionFind(n)
        result=0
        count=n-1
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost=abs(x1-x2) + abs(y1-y2)
                edge=Edge(i,j,cost)
                pq.append(edge)
        
        heapq.heapify(pq)
        
        while pq and count>0:
            edge=heapq.heappop(pq)
            if uf.union(edge.point1, edge.point2):
                result+=edge.cost
                count-=1
        
        return result
    
    
    
    