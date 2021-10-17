class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        '''Usig XOR'''
        # xor of a number with itself returns 0
#         res=0
#         for i in nums:
#             res^=i
#         return res
        
        return reduce(lambda x,y: x^y, nums)
        
        
        '''Extra Space'''
        #return 2*sum(set(nums))-sum(nums)
        
        #Using dictionary
        d=dict()
        for i in nums:
            d[i]=d.get(i,0)+1
        for key,value in d.items():
            if value==1:
                return key