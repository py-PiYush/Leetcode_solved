class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums))<len(nums)
        
#         from collections  import Counter
        
#         cnt=Counter(nums)
#         for i in cnt.values():
#             if i>1:
#                 return True
#         return False
    