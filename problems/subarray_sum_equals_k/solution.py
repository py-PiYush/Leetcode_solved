class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    
        ans=0
        countPref={0:1}
        pref=0
        for i in range(len(nums)):
            pref+=nums[i]
            need=pref-k
            if need in countPref:
                ans+=countPref[need]
            countPref[pref]=countPref.get(pref,0)+1
        return ans