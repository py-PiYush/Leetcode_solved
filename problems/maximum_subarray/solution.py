class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         result, curSum = nums[0], 0
        
#         for i in range(len(nums)):
#             if curSum < 0:
#                 curSum = 0
#             curSum += nums[i]
#             result = max(result, curSum)
        
#         return result
        
        # for i in range(1,len(nums)):
        #     nums[i]=max(nums[i], nums[i]+nums[i-1])
        # return max(nums)
        
        
        '''Divide and Conquer (As given in CLRS)'''
        '''O(nlogn)'''
#         def maxCrossSubarray(A, low, mid, high):
#             left_sum=-math.inf
#             sum_=0
#             max_left=mid
#             for i in reversed(range(low,mid+1)):
#                 sum_+=A[i]
#                 if sum_>left_sum:
#                     left_sum=sum_
#                     max_left=i
#             sum_=0
#             right_sum=-math.inf
#             max_right=mid+1
#             for i in range(mid+1, high+1):
#                 sum_+=A[i]
#                 if sum_>right_sum:
#                     right_sum=sum_
#                     max_right=i
#             return (max_left, max_right, left_sum+right_sum)
        
#         def findMaxSubarray(A,low,high):
#             if low==high:
#                 return low, high, A[low]
#             mid=(low+high)//2
#             left_low, left_high, left_sum=findMaxSubarray(A,low,mid)
#             right_low, right_high, right_sum=findMaxSubarray(A,mid+1, high)
#             cross_low, cross_high, cross_sum=maxCrossSubarray(A,low,mid,high)
            
#             if left_sum==max(left_sum, right_sum, cross_sum):
#                 return (left_low, left_high, left_sum)
#             elif right_sum==max(left_sum, right_sum, cross_sum):
#                 return (right_low, right_high, right_sum)
#             else:
#                 return (cross_low, cross_high, cross_sum)
        
#         _,_,maxSum=findMaxSubarray(nums, 0, len(nums)-1)
#         return maxSum
    
    
        '''Divide and Conquer O(n)'''
        def dac(l,r):
            if l==r:
                return nums[l],nums[l], nums[l], nums[l]
            
            mid=(l+r)//2
            head_sum_l, tail_sum_l, sum_l, maxSum_l=dac(l,mid)
            head_sum_r, tail_sum_r, sum_r, maxSum_r=dac(mid+1,r)
            
            head_sum=max(head_sum_l, sum_l+head_sum_r)
            tail_sum=max(tail_sum_r, sum_r+tail_sum_l)
            sum_=sum_l+sum_r
            
            maxSum=max(maxSum_l, maxSum_r, tail_sum_l+head_sum_r)
            
            return head_sum, tail_sum, sum_, maxSum
        _,_,_,maxSum=dac(0,len(nums)-1)
        return maxSum