class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''if sum(0,i)%k==sum(0,j)%k then
            sum(i,j) is divisible by k'''
        cnt=0
        d=[1]+[0]*(k-1)
        run=0
        for n in nums:
            run=(run+n)%k
            if d[run]:
                cnt+=d[run]
            d[run]+=1
        return cnt
        
        
        
        '''Brute Force'''
        cnt=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if sum(nums[i:j])%k==0:
                    cnt+=1
        return cnt