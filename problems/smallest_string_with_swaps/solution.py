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
        
            
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        uf=UnionFind(n)
        
        #we can build connected components where each component is a list of indices that
        #can be exchanged with any of them.
        for x,y in pairs:
            uf.union(x,y)
            
        result=[]
        map_=defaultdict(list)
        
        #for every absolute root, maintain a sorted list of char.
        for i in range(n):
            map_[uf.find(i)].append(s[i])
        for key in map_.keys():
            map_[key].sort(reverse=True)
        
        #for each index we locate its absolute root and grab the next lowest character
        #from the list corresponding to that root.
        for i in range(n):
            result.append(map_[uf.find(i)].pop())
        
        return ''.join(result)
            