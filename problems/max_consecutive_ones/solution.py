from itertools import groupby
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # res=[]
        # for i,j in groupby(nums):
        #     if int(i)==1:
        #         res.append(len(list(j)))
        # if len(res)==0:
        #     return 0
        # return max(res)
        
        cnt=0
        max_=0
        for i in range(len(nums)):
            if int(nums[i])==1:
                cnt+=1
                max_=max(max_,cnt)
                print(max_)
            else:
                cnt=0
                
        max_=max(max_,cnt)
        return max_