class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ''' Using extra space '''
        cnt = Counter(nums)
        return [k for k,v in cnt.items() if v==1]