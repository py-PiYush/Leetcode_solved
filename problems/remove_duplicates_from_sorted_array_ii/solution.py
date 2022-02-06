class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        '''two pointers'''
        if len(nums) < 2: return len(nums)
        slow, fast = 2, 2

        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
        
        
        ''' using counter '''
        cnt=Counter(nums)
        i=0
        for n in cnt:
            if cnt[n]>=2:
                nums[i:i+2]=[n]*2
                i+=2
            else:
                nums[i]=n
                i+=1
        return i
                