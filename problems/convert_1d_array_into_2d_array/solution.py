class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res=[]
        if m*n!=len(original):
            return res
        for i in range(1,m+1):
            res.append(original[(i-1)*n:i*n])
            
        return res