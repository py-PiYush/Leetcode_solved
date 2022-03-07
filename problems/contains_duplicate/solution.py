class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums)>len(set(nums))
    
    
        '''---USING SET---'''
        seen=set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False