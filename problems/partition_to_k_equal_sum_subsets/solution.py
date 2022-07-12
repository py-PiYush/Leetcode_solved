class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        ''' 2 choice for every index for k subsets O(k*2^n)'''
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
        
        
        ''' k choices for every index O(k^n)'''
        total = sum(nums)
        if total%k!=0:
            return False
        req_sum = total//k
        subsets_sum = [0]*k
        
        nums.sort(reverse=True)
        def recur(idx):
            if idx == len(nums):
                return all(subsets_sum[i]==req_sum for i in range(k))
            
            for i in range(k):
                if subsets_sum[i] + nums[idx] <= req_sum:
                    subsets_sum[i]+=nums[idx]
                    if recur(idx+1):
                        return True
                    subsets_sum[i]-=nums[idx]
                # else:
                #     if recur(idx+1):
                #         return True
            return False
        
        return recur(0)
                    