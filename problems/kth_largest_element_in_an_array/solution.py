import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        '''Sorted list O(N)'''
        # return sorted(nums, reverse=True)[k-1]
        
        '''Quick Select O(N) average'''
#         if not nums: return
#         pivot = random.choice(nums)
#         left =  [x for x in nums if x > pivot]
#         mid  =  [x for x in nums if x == pivot]
#         right = [x for x in nums if x < pivot]
        
#         L, M = len(left), len(mid)
        
#         if k <= L:
#             return self.findKthLargest(left, k)
#         elif k > L + M:
#             return self.findKthLargest(right, k - L - M)
#         else:
#             return mid[0]
    
        '''min heap'''
        import heapq
        # pq=nums[:k]
        # heapq.heapify(pq)
        # for x in nums[k:]:
        #     heapq.heappushpop(pq, x)
        # return pq[0]
        
        '''nlargest'''
        return(heapq.nlargest(k,nums))[-1]
        