class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums, start, end):
            if start >= end:
                return 0
            mid = (start+end)//2 + 1
            count = mergeSort(nums, start, mid-1) + mergeSort(nums, mid, end)
            j = mid 
            for i in range(start, mid):
                while j<=end and nums[j]*2 < nums[i]:
                    j += 1
                count += (j-mid)
            nums[start:end+1] = sorted(nums[start:end+1])
            return count
        return mergeSort(nums, 0, len(nums)-1)
        
        
        
        
        ''' Merge sort based'''
        self.cnt = 0
        def mergeSort(nums):
            def merge(nums,L,R):
                l, r = 0, 0                         # increase l and r iteratively
                while l < len(L) and r < len(R):
                    if L[l] <= 2*R[r]:
                        l += 1
                    else:
                        self.cnt += len(L)-l     # COUNT here
                        r += 1
                i = j = k = 0
                while i < len(L) and j < len(R): 
                    if L[i] <= R[j]: 
                        nums[k] = L[i] 
                        i+=1
                    else: 
                        nums[k] = R[j]
                        j+=1
                    k+=1

                while i < len(L): 
                    nums[k] = L[i] 
                    i+=1
                    k+=1

                while j < len(R): 
                    nums[k] = R[j] 
                    j+=1
                    k+=1

            if len(nums)>1:
                    mid=len(nums)//2
                    L=nums[:mid]
                    R=nums[mid:]
                    mergeSort(L)
                    mergeSort(R)
                    merge(nums,L,R)
        mergeSort(nums)
        return self.cnt
        
        
        ''' Brute Force '''
        cnt=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>2*nums[j]:
                    cnt+=1    
        return cnt