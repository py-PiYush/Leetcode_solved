class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ''' (1-indexed) Visit all the indexes present in nums and mark them negative 
            The index at which elem remains positive will be absent.
        
        '''
        for num in nums:
            index = abs(num)-1
            nums[index] = -abs(nums[index])
        
        return [i+1 for i, n in enumerate(nums) if n>0]
        
        
        #sets
        res=[]
        '''set_=set(nums)
        for i in range(1,len(nums)+1):
            if i not in set_:
                res.append(i)
        return res'''
    
        #Hash_maps for constant lookup time
        maps={}
        for i in nums:
            maps[i]=1
        for i in range(1,len(nums)+1):
            if i not in maps:
                res.append(i)
        return res