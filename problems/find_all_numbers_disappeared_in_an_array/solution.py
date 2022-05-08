class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
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