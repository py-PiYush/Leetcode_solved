class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''Kadane's'''
        pre,suf,max_so_far=0,0,float('-inf')
        for i in range(len(nums)):
            pre=(pre or 1)*nums[i]
            suf=(suf or 1)*nums[~i]
            max_so_far=max(max_so_far,pre,suf)
        return max_so_far
        
        
        
        '''Brute Force'''
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                cur=1
                for k in range(i,j):
                    cur*=nums[k]
                res.append(cur)
        return max(res)
        