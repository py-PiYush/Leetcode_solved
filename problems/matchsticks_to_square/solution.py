class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ''' Using 698.partition to k equal sum subset'''
        nums, k = matchsticks, 4
        total = sum(nums)
        if total%k!=0:
            return False
        req_sum = total//k
        nums.sort(reverse=True)
        used = [False]*len(nums)
        
        def recur(idx, k, subset_sum):
            if k==1: return True
            if subset_sum == req_sum: return recur(0, k-1, 0)
            
            for i in range(idx, len(nums)):
                if i > 0 and not used[i -1] and nums[i] == nums[i - 1]:
                    continue
                if not used[i] and subset_sum + nums[i] <= req_sum:
                    used[i]=True
                    if recur(i+1, k, subset_sum+nums[i]):
                        return True
                    used[i]=False
            return False
        return recur(0,k,0)