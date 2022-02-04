class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
        ''' Same as previous sol but not using prefix sum array'''
        count = 0
        max_length=0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index
        
        return max_length
        
        

        
        ''' 
        Initial approach:
        Replace 0 with -1 and form a prefix sum array
        If sum of any contiguous subarray is 0, that subarray is 
        potential candidate for answer.
        '''
        new=[1 if n==1 else -1 for n in nums ]
        pre=[0]
        for i in range(len(new)):
            pre.append(pre[i]+new[i])
        print(pre)
        
        maps={}
        maxLen=0
        for i in range(len(pre)):
            if pre[i] in maps:
                maxLen=max(maxLen, abs(maps[pre[i]]-i))
            else:
                maps[pre[i]]=i
        
        return maxLen