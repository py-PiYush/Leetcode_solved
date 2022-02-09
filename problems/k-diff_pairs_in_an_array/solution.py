class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        cnt=Counter(nums)
        if k==0: return sum(i>=2 for i in cnt.values())
        
        set_=set(nums)
        ans=0
        for n in set_:
            if n+k in set_:
                ans+=1
        return ans
        
        
        ''' Brute force'''
        ans=0
        seen=set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j])==k:
                    if (nums[i], nums[j]) not in seen and (nums[j], nums[i]) not in seen:
                        ans+=1
                        seen.add((nums[i], nums[j]))
        return ans