class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        '''sorting to avoid duplicates'''
        def dfs(nums, path):
            if not nums:
                ans.append(path[:])
                return 
            
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        nums.sort()    
        ans=[]
        dfs(nums, [])
        return ans
        
        
        '''Hash table'''
        count=Counter(nums)
        ans=[]
        
        def dfs(path):
            if len(path)==len(nums):
                ans.append(path[:])
                return 
            
            for n in count:
                if count[n]>0:
                    count[n]-=1
                    dfs(path+[n])
                    count[n]+=1
            
        dfs([])
        return ans