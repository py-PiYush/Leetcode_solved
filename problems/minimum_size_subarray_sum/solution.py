class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        '''Sliding window'''
        l=sum_=0
        ans=len(nums)+1
        for i in range(len(nums)):
            sum_+=nums[i]
            while sum_>=target:
                ans=min(ans, i-l+1)
                sum_-=nums[l]
                l+=1
        return ans if ans!=len(nums)+1 else 0
        
        
        '''Brute Force (TLE)'''
        
        # ans=float('inf')
        # flag=False
        # for i in range(len(nums)):
        #     sum_=0
        #     for j in range(i, len(nums)):
        #         sum_+=nums[j]
        #         if sum_>=target:
        #             flag=True
        #             ans=min(ans, j-i+1)
        #             break
        # return ans if flag else 0