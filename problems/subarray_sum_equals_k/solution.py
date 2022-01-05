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
    
    
        ''' prefix sum (prefixSum[i->j] = prefixSum[j]-prefixSum[i-1])
            
            TLE
        '''
        cnt=0
        for i in range(len(nums)):
            pref=0
            for j in range(i,  len(nums)):
                pref+=nums[j]
                if pref==k:
                    cnt+=1
        return cnt