class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        cnt1 = Counter(a+b for a in nums1 for b in nums2)
        cnt2 = Counter(c+d for c in nums3 for d in nums4)
        ans=0
        
        for val in cnt1:
            if -val in cnt2:
                ans+=cnt1[val]*cnt2[-val]
        
        return ans