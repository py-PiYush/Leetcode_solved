class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for x in nums: 
            if x == 0: return 0 
            if x < 0: ans *= -1
        return ans 
        
        
        
        '''-------------'''
        if 0 in nums: return 0
        count_negative = sum(n<0 for n in nums)
        return (1, -1)[count_negative%2!=0]