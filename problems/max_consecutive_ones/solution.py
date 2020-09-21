from itertools import groupby
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=[]
        for i,j in groupby(nums):
            if int(i)==1:
                res.append(len(list(j)))
        if len(res)==0:
            return 0
        return max(res)
        