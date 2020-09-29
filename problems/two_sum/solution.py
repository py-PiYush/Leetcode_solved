class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps={}
        for i in range(len(nums)):
            if nums[i] in maps:
                return maps[nums[i]],i
                
            find=target-nums[i]
            if find not in maps:
                maps[find]=i
            
                    
        