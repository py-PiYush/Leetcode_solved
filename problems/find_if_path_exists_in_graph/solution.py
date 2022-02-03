class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.rank = [1]*size
        
    def find(self, x):
        if self.parent[x]==x:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        X=self.find(x)
        Y=self.find(y)
        if X==Y: return
        if self.rank[X]>self.rank[Y]:
            self.parent[Y]=X
        elif self.rank[X]<self.rank[Y]:
            self.parent[X]=Y
        else:
            self.parent[X]=Y
            self.rank[Y]+=1
        
    def connected(self, x, y):
        return self.find(x)==self.find(y)
            

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ''' Union Find '''
        uf=UnionFind(n)
        for a,b in edges:
            uf.union(a,b)
        return uf.connected(source, destination)
        
        
        
        ''' BFS '''
        adj_list=[[] for _ in range(n)]
        seen=set()
        
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            
        queue=deque([source])
        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            if node in seen:
                continue
            seen.add(node)
            for neighbour in adj_list[node]:
                queue.append(neighbour)
        
        return False
        
        
        
        
        ''' iterative dfs (card sol)'''
        adj_list=[[] for _ in range(n)]
        seen=set()
        
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            
        stack=[source]
        
        while stack:
            node=stack.pop()
            if node==destination:
                return True
            if node in seen:
                continue
            seen.add(node)
            
            for neighbour in adj_list[node]:
                stack.append(neighbour)
        
        return False
                