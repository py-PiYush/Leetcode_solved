class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        ans, suf, pre = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre               # prefix product from one end
            pre *= nums[i]
            ans[-1-i] *= suf            # suffix product from other end
            suf *= nums[-1-i]
        return ans
        
        
        
        '''Prefix and suffix product'''
        pre, suf, n = list(accumulate(nums, mul)), list(accumulate(nums[::-1], mul))[::-1], len(nums)
        return [(pre[i-1] if i else 1) * (suf[i+1] if i+1 < n else 1) for i in range(n)]
        
        
        
        '''Using division operator'''
        countZero=nums.count(0)
        if countZero>=2:
            return [0]*len(nums)
        nonZeroProd=1
        for n in nums:
            if n!=0:
                nonZeroProd*=n
        if countZero:
            res=[0 if n!=0 else nonZeroProd for n in nums]
        else:
            res=[nonZeroProd//n for n in nums]
            
        return res