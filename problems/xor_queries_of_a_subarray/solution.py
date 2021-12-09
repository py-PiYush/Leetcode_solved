class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefXor=[arr[0]]
        for i in range(1,len(arr)):
            cur=prefXor[-1]
            prefXor.append(cur^arr[i])
        print(prefXor)
        res=[]
        for l,r in queries:
            res.append(prefXor[r] if l==0 else prefXor[r]^prefXor[l-1])
        return res