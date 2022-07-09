class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        
        limit = 10**5
        diff = [0]*(limit+1)
        for i in range(len(nums1)):
            diff[abs(nums1[i]-nums2[i])]+=1
        n=len(nums1)
        acc, val, changes = 0,0,k1+k2
        for i in range(limit, -1, -1):
            acc = diff[i]
            if acc<=changes:
                if i<=1: return 0
                diff[i-1]+=diff[i]
                diff[i]=0
                changes-=acc
            else:
                if i==0: return 0
                diff[i]-=changes
                diff[i-1]+=changes
                break
        ans = 0
        for i in range(1, limit+1):
            ans+=diff[i]*(i*i)
        return ans