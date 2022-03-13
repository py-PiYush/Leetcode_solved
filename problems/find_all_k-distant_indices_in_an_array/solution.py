class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_idx = []
        result = set()
        for i in range(len(nums)):
            if nums[i] == key:
                key_idx.append(i)
        
        for i in range(len(nums)):
            for idx in key_idx:
                if abs(i-idx)<=k:
                    result.add(i)
        return result