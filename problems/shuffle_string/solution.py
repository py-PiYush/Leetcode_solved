class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newarr=zip(indices,list(s))
        res=sorted(newarr,key=lambda x:x[0])
        shfld=''.join([i[1] for i in res])
        return shfld