from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        '''Iterative'''
        ret = [[]]
        for n in nums:
            ret += [r + [n] for r in ret]
        return ret
        
        '''Bitmask'''
        n=len(nums)
        ans=[]
        for i in range(2**n, 2**(n+1)):
            bitmask=bin(i)[3:]
            ans.append([nums[j] for j in range(n) if bitmask[j]=='1'])
        return ans
        
        
        '''Using combinations'''
        # res=[]
        # for i in range(len(nums)+1):
        #     res+=map(list,combinations(nums,i))
        # return res
        
        
        '''Bactracking'''
        def backtrack(first=0, cur=[]):
            if len(cur)==k:
                ans.append(cur[:])
                return
            
            for i in range(first, n):
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()
        
        ans=[]
        n=len(nums)
        
        #combinations of length k
        for k in range(n+1):
            backtrack()
        return ans
        
        '''Recursion'''
        def helper(arr, idx):
            if idx==len(nums):
                ans.append(arr)
                return 
            elem=nums[idx]
            helper(arr+[elem], idx+1)
            helper(arr, idx+1)
        
        ans=[]
        helper([], 0)
        return ans