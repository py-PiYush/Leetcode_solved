class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
#         m={}
#         prefix, suffix = [0], [0]
#         for i in range(len(nums)):
#             prefix+=[prefix[i]+nums[i]]
#             suffix+=[suffix[i]+nums[-i-1]]
#         # print(prefix, suffix)
        
#         for i,n in enumerate(prefix):
#             if n<=x:
#                 m[x-n]=i
#         res=[]
#         for i,n in enumerate(suffix):
#             if n in m and i+m[n]<=len(nums):
#                 res.append(i+m[n])
#         # print(m)
#         # print(res)
#         return min(res) if res else -1
    
    
        '''Same idea as above but insted of prefix+suffix=x, find longest subarray and
        such that sum(nums)-x = subarray sum.'''
        ans=-float('inf')
        left=curSum=found=0
        target = sum(nums)-x
        for right in range(len(nums)):
            curSum+=nums[right]
            while left<=right and curSum>target:
                curSum-=nums[left]
                left+=1
            if curSum==target:
                found=1
                ans=max(ans, right-left+1)
        return len(nums)-ans if found else -1
            
        
        
        
        '''Recursion w memoization (TLE)'''
        @lru_cache()
        def rec(l, r, x, cnt):
            if x == 0: return cnt
            if l>r or x<0: return float('inf')
            lm = rec(l+1, r, x-nums[l], cnt+1)
            rm = rec(l, r-1, x-nums[r], cnt+1)
            return min(lm, rm)
        
        res = rec(0,len(nums)-1, x, 0)
        return res if res!=float('inf') else -1