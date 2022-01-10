class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(idx, arr):
            if idx==len(nums):
                ans.append(arr[:])
                return
            
            #All subsets which include nums[idx]
            backtrack(idx+1, arr+[nums[idx]])
            
            #All subsets which don't include nums[idx]
            
            #skipping duplicates
            while idx+1<len(nums) and nums[idx]==nums[idx+1]:
                idx+=1
            
            backtrack(idx+1, arr)
        
        nums.sort()
        ans=[]
        backtrack(0,[])
        return ans
        
        
        
        '''
        Using choose/not choose with a set to keep
        track of subsets already in ans
        '''
        def helper(arr, idx):
            if idx==len(nums):
                if tuple(arr) not in s:
                    ans.append(arr)
                    s.add(tuple(arr))
                return 
            elem=nums[idx]
            helper(arr+[elem], idx+1)
            helper(arr, idx+1)
        
        ans=[]
        s=set()
        nums.sort()
        helper([], 0)
        return ans