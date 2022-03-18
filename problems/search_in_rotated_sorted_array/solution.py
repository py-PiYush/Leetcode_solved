class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ''' ----- Find mid of real Array -------'''
        n = len(nums)
        #Find Pivot index
        start, end, pivot = 0, n-1, 0
        while start<end:
            mid = start + (end-start)//2
            if nums[mid]>nums[end]:
                start = mid + 1
            else:
                end = mid
        pivot = start
        
        # Find the mid of the real array during binary search
        start, end = 0, n-1
        while start<=end:
            mid = start + (end-start)//2
            real_mid = (mid + pivot)%n
            if nums[real_mid]==target:
                return real_mid
            elif nums[real_mid]<target:
                start=mid+1
            else:
                end=mid-1
                
        return -1
        
        
        
        '''-------- 3 binary searches --------'''
        n = len(nums)
        #Find Pivot index
        start, end, pivot = 0, n-1, 0
        while start<end:
            mid = start + (end-start)//2
            if nums[mid]>nums[end]:
                start = mid + 1
            else:
                end = mid
        pivot = start
            
        #Search in left of pivot
        start, end = 0, pivot-1
        while start<end:
            mid = start + (end-start)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                start = mid+1
            else:
                end=mid
        if nums[start]==target: return start
        
        #Search in right of pivot(inclusive)
        start, end = pivot, n-1
        while start<end:
            mid = start + (end-start)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                start = mid+1
            else:
                end=mid
        if nums[start]==target: return start
        
        return -1
        
        
        
        
        '''---- Not O(logn) ------'''
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1