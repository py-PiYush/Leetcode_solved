class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        i=0
        max_len=max(len(index),len(nums))
        #min_len=min(len(index),len(nums))
        while i<max_len:
            target.insert(index[i],nums[i])
            i+=1
                
        return target    
            