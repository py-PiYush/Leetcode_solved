class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        ''' Binary search '''
        def condition(dist):
            count, i, j = 0,0,0
            while i<len(nums) or j <len(nums):
                while j<len(nums) and nums[j] - nums[i]<=dist:
                    j+=1
                count+=j-i-1
                i+=1
            return count >= k
        
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left<right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid+1
        return left
        
        
        ''' Brute Force (TLE)'''
        distances = [abs(nums[i] - nums[j]) for i in range(len(nums)) for j in range(i+1, len(nums))]
        distances.sort()
        return distances[k-1]