class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #Using Counter
#         from collections import Counter
        
#         lst=Counter(nums)
#         mj=len(nums)//2
#         for i in lst:
#             if lst[i]>mj:
#                 return i
        
        #Boyer-Moore:
        # def bm():
        #     cnt=0
        #     for i in nums:
        #         if cnt==0:
        #             ans=i
        #         cnt+=(1 if i==ans else -1)
        #     return ans
        # return bm()
        
        
                
        def solve(lo,hi):
            mid=lo+((hi-lo)//2)
            if lo==hi:
                return nums[lo]
            leftmj=solve(lo,mid)
            rightmj=solve(mid+1,hi)
            if leftmj==rightmj:
                return leftmj
            lftcnt=sum(1 for i in range(lo,hi+1) if nums[i]==leftmj)
            rtcnt=sum(1 for i in range(lo,hi+1) if nums[i] == rightmj)
            return leftmj if lftcnt>rtcnt else rightmj
        return solve(0,len(nums)-1)