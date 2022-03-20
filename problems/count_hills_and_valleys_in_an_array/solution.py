class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        cnt, left = 0, nums[0]
        for i in range(1, len(nums)-1):
            if (left<nums[i] and nums[i]>nums[i+1]) or (left>nums[i] and nums[i]<nums[i+1]):
                cnt+=1
                left=nums[i]
        return cnt
        
        '''------------'''
        hill, valley, cnt = False,False,0
        
        for i in range(1, len(nums)):
            if nums[i-1]<nums[i]:
                hill = True
                if valley:
                    cnt+=1
                    valley=False
            if nums[i]<nums[i-1]:
                valley = True
                if hill:
                    cnt+=1
                    hill = False
        return cnt