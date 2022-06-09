class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''negative marking'''
        res =[]
        for n in nums:
            idx=abs(n)-1
            if nums[idx]<0:
                res.append(idx+1)
            else:
                nums[idx]*=-1
        return res
        
        ''' swap sort '''
        i=0
        while i<len(nums):
            idx=nums[i]-1
            if idx!=i and nums[idx]!=nums[i]:
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i+=1
        # print(nums)
        return [n for i,n in enumerate(nums) if i!=n-1]
        
        
        '''Using set, O(n) extra space '''
        seen=set()
        res = []
        for n in nums:
            if n in seen:
                res.append(n)
            seen.add(n)
        return res