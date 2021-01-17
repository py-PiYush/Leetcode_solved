class Solution:
    def countBits(self, num: int) -> List[int]:
        res=[]
        for i in range(num+1):
            cnt=0
            while i:
                cnt+=1
                i=i&(i-1)
            res.append(cnt)
        return res