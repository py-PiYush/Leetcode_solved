class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.selectionSort(nums)
        # self.bubbleSort(nums)
        # self.insertionSort(nums)
        # self.mergeSort(nums)       
        self.quickSort(nums)
        return nums
    
    ''' 
    Selection Sort (TLE)
    TC: O(n^2) ;  SC: O(1), in-place
    Not Stable
    Minimum swaps
    '''
    def selectionSort(self, nums):
        for i in range(len(nums)):
            min_idx=i
            for j in range(i, len(nums)):
                if nums[j]<nums[min_idx]:
                    min_idx=j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            
    '''
    Bubble Sort (TLE)
    TC: best-O(n), worst-O(n^2)
    SC: O(1)
    Stable
    Use when array is almost sorted
    '''
    def bubbleSort(self, nums):
        for i in range(len(nums)):
            swapped = False
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            
            if not swapped:
                break
                
    '''
    Insertion Sort (TLE)
    TC: best-O(n), worst-O(n^2)
    SC: O(1)
    Stable
    '''
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j=i-1
            while j>=0 and key<nums[j]:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
    
    '''
    Merge Sort
    Recursive
    TC: O(nlogn)
    SC: O(n)
    Stable
    '''
    def mergeSort(self, nums):
        def merge(nums,L,R):
            i = j = k = 0
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
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
                self.mergeSort(L)
                self.mergeSort(R)
                merge(nums,L,R)
        
    '''
    QuickSort
    Recursive
    TC: average-O(nlogn), worst-O(n^2)
    SC: O(n) recursion stack, in-place
    Not stable
    '''
    def quickSort(self, nums):
        # 3-way randomized
        def partition(l, r):
            pivot_idx = random.choice(range(l,r+1))
            pivot = nums[pivot_idx]
            # print(pivot)
            left, move, right = l,l,r
            while move<=right:
                if nums[move]<pivot:
                    nums[left], nums[move] = nums[move], nums[left]
                    move+=1
                    left+=1
                elif nums[move]>pivot:
                    nums[right], nums[move] = nums[move], nums[right]
                    right-=1
                else:
                    move+=1
            return left-1, move
        
        def quicksort(nums, low, high):
            if low<high:
                l,r = partition(low, high)
                quicksort(nums, low, l)
                quicksort(nums, r, high)
                
        quicksort(nums, 0, len(nums)-1)
        
        #---------------------------------------------------------------
        # def helper(head, tail):
        #     if head >= tail: return 
        #     l, r = head, tail
        #     m = (r - l) // 2 + l
        #     pivot = nums[m]
        #     while r >= l:
        #         while r >= l and nums[l] < pivot: l += 1
        #         while r >= l and nums[r] > pivot: r -= 1
        #         if r >= l:
        #             nums[l], nums[r] = nums[r], nums[l]
        #             l += 1
        #             r -= 1
        #     helper(head, r)
        #     helper(l, tail)

        # helper(0, len(nums)-1)
