class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []
        for i in nums:
            if res and res[-1][1] == i-1:
                res[-1][1] = i
            else:
                res.append([i,i])
        return [str(x)+"->"+str(y) if x!=y else str(x) for x,y in res]
        
        
        
        '''----------------------'''
        result = []
        nums.append(float('inf'))
        start = str(nums[0])
        
        for i in range(len(nums)):
            if i > 0 and nums[i]-1 != nums[i-1]:
                if int(start) != nums[i-1]:
                    result.append(start + '->' + str(nums[i-1]))
                else:
                    result.append(start)
                start = str(nums[i])
                
        return result