class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        '''----------------'''
        nan = float('nan')
        diffs = [a-b for a, b in zip([nan] + nums, nums + [nan]) if a-b]
        return sum(not d*e >= 0 for d, e in zip(diffs, diffs[1:]))
    
        ''' DP '''
        if len(nums)<2:
            return len(nums)
        up, down = [1]*len(nums), [1]*len(nums)
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                up[i] = down[i-1]+1
                down[i]=down[i-1]
            elif nums[i]<nums[i-1]:
                down[i]=up[i-1]+1
                up[i]=up[i-1]
            else:
                down[i]=down[i-1]
                up[i]=up[i-1]
        return max(up[len(nums)-1], down[len(nums)-1])
        
        ''' Brute force O(n!)'''
        @lru_cache()    #Memoize
        def calc(idx, isUp):
            max_cnt = 0
            for i in range(idx+1, len(nums)):
                if isUp and nums[i]>nums[idx] or not isUp and nums[i]<nums[idx]:
                    max_cnt = max(max_cnt, 1+ calc(i,not isUp))
            return max_cnt
        
        if len(nums)<2:
            return len(nums)
        return 1+max(calc(0,True), calc(0, False))