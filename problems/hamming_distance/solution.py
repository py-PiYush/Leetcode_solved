class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res=x^y
        dis=0
        while res:
            dis+=res&1
            res=res>>1
        return dis
            