class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        
        # from itertools import permutations
        # return list(permutations(nums))
        res=[]
        self.dfs(nums, [], res)
        return res
    
    def dfs(self,nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            #removing nums[i] from arr
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
        
        
        
        
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
                
        ans = []
        backtrack(0, len(nums))
        return ans