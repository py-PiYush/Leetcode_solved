class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        '''---'''
        res = []
        q = deque([])
                
        
        
        for i in range(len(nums)):
            while  q and q[-1][0]<nums[i]:
                q.pop()
            q.append((nums[i],i))
            if i-k==q[0][1]:
                q.popleft()
            if i>=k-1:
                res.append(q[0][0])
        return res
        
        
        ''' Brute force O(n*k)'''
        res = []
        for left in range(len(nums)-k+1):
            res.append(max(nums[left:left+k]))
        return res