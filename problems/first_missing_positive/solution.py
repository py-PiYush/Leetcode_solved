class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''best'''
        """:type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range
        [1,...,l+1], so we only have to care about those elements in this range and
        remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number
        within the range [1,...,l+1] 
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]//n==0:
                return i
        return n
        
        
        
        ''' Negative marking(see find duplicate) linear time constant space ---- (HARD)'''
        
        #solution space [1, len(nums)+1]
        
        #replace negatives
        size = len(nums)
        for i in range(size):
            if nums[i]<0:
                nums[i]=0
        
        #Keep track of occured numbers by negative marking
        for n in nums:
            i = abs(n)-1
            if i>=0 and i<size and nums[i]>=0:
                if nums[i]==0:
                    nums[i]=-(size+1)
                else:
                    nums[i]=-nums[i]
        print(nums[size-3:])
        #check for every ans in solution space
        for ans in range(1, size+1):
            idx=ans-1
            if nums[idx]>=0:
                return ans
        return size+1
        
        
        ''' sorting time O(nlogn)'''
        nums.sort()
        ans=1
        for n in nums:
            if ans==n:
                ans+=1
            elif ans<n:
                return ans
        
        
        ''' Using set, O(N) extra space'''
        s=set(nums)
        for i in range(1, 5*10**5 + 2):
            if i not in s:
                return i
            