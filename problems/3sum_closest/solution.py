class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        '''Two pointers'''
        nums.sort()
        result=sum(nums[:3])
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i+1, len(nums)-1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == target:
                    return summ
                
                if abs(summ-target) < abs(result-target):
                    result=summ
                    
                elif summ < target:
                    l+=1
                else:
                    r-=1
                    
        return result
        
        
        
        '''Brute Force (TLE)'''
        min_diff=float('inf')
        ans=0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    summ=nums[i]+nums[j]+nums[k]
                    if abs(target-summ)<min_diff:
                        min_diff = abs(target - summ)
                        ans=summ
        return ans