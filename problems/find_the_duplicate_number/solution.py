class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        '''O(n) space'''
#         s=set()
#         for i in nums:
#             if i in s:
#                 return i
#             s.add(i)
            
            
        '''Negative marking'''
        # for num in nums:
        #     cur=abs(num)
        #     if nums[cur]<0:
        #         return cur
        #     nums[cur]=-nums[cur]
        
        '''Array as Hashmap'''
        # def store(nums,cur):
        #     if nums[cur]==cur:
        #         return cur
        #     nxt=nums[cur]
        #     nums[cur]=cur
        #     return store(nums,nxt)
        # return store(nums,0)
        
        '''Binary Search'''
#         def condition(cur):
#             count=sum(num<=cur for num in nums)
#             if count>cur:
#                 return True
#             return False
        
#         left,right=1,len(nums)-1
#         while left<right:
#             mid=left + (right-left)//2
#             if condition(mid):
#                 right=mid
#             else:
#                 left=mid+1
#         return left
        
        
        '''Floyd's cycle detection '''
        slow=fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
        
        
            