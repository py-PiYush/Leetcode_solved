class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, max_=0,0
        for i in nums:
            if i==1:
                cnt+=1
                max_=max(max_, cnt)
            else:
                cnt=0
        return max_
        