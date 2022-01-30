class UnionFind:
    def __init__(self, size):
        self.root=[i for i in range(size)]
        self.rank=[1]*size
        self.count=size
    
    def find(self, x):
        if self.root[x]==x:
            return x
        self.root[x]=self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootX=self.find(x)
        rootY=self.find(y)
        if rootX!=rootY:
            if self.rank[rootX]>self.rank[rootY]:
                self.root[rootY]=rootX
            elif self.rank[rootX]<self.rank[rootY]:
                self.root[rootX]=rootY
            else:
                self.root[rootY]=rootX
                self.rank[rootX]+=1
            self.count-=1
        
            
    def connected(self, x, y):
        return self.find(x)==self.find(y)
            
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ''' dfs '''
        n=len(isConnected)
        def dfs(i):
            for j, adj in enumerate(isConnected[i]):
                if adj and j not in seen:
                    seen.add(j)
                    dfs(j)
        
        seen=set()
        ans=0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans+=1
        return ans
        
        
        ''' discussion sol'''
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        n = len(isConnected)
        uf = {i:i for i in range(n)}
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    uf[find(i)] = find(j)
        
        return sum([1 for k, v in uf.items() if k == v])
        
        
        
        
        ''' Graph card sol '''
        n=len(isConnected)
        uf=UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    uf.union(i,j)
        return uf.count
        
        