class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)
        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results
        
                                 
        '''------------------------------------------------------------------'''
#         def kSum(nums, target, k):
#             res=[]
#             if not nums:
#                 return res
            
#             average=target//k
#             if average<nums[0] or average>nums[-1]:
#                 return res
            
#             if k==2:
#                 return twoSum(nums, target)
            
#             for i in range(len(nums)):
#                 if i==0 or nums[i-1]!=nums[i]:
#                     for subset in kSum(nums[i+1:], target-nums[i], k-1):
#                         res.append([nums[i]]+subset)
#             return res
        
#         def twoSum(nums, target):
#             res=[]
#             lo,hi=0, len(nums)-1
#             while lo<hi:
#                 cur_sum=nums[lo]+nums[hi]
#                 if cur_sum<target or (lo>0 and nums[lo]==nums[lo-1]):
#                     lo+=1
#                 elif cur_sum>target or (hi< len(nums)-1 and nums[hi]==nums[hi+1]):
#                     hi-=1
#                 else:
#                     res.append([nums[lo], nums[hi]])
#                     lo+=1
#                     hi-=1
#             return res
        
#         nums.sort()
#         return kSum(nums, target, 4)