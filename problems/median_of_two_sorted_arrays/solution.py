class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''Binary Search O(log(min(m,n)))'''
        
        x,y=len(nums1), len(nums2)
        if x>y:
            return self.findMedianSortedArrays(nums2, nums1)
        
        left, right = 0, x
        while left<right:
            partitionX = left + (right-left)//2
            partitionY = (x+y+1)//2 - partitionX
            
            maxLeftX = nums1[partitionX-1] if partitionX>0 else -float('inf')
            minRightX = nums1[partitionX] if partitionX<x else float('inf')
            
            maxLeftY = nums2[partitionY-1] if partitionY>0 else -float('inf')
            minRightY = nums2[partitionY] if partitionY<y else float('inf')
            
            if maxLeftX<=minRightY and maxLeftY<=minRightX:
                if (x+y)%2==0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                else:
                    return max(maxLeftX, maxLeftY)
            
            elif maxLeftX>minRightY:
                right=partitionX
            else:
                left=partitionX+1
        
        
        
        
        ''' Merge in linear time O(m+n)'''
        
        def merge(nums1, nums2):
            new=[]
            i,j,k=0,0,0
            while i<len(nums1) and j<len(nums2):
                if nums1[i]<=nums2[j]:
                    new.append(nums1[i])
                    i+=1
                else:
                    new.append(nums2[j])
                    j+=1
            new+=nums1[i:]
            new+=nums2[j:]
            return new
        
        new=merge(nums1, nums2)
        n=len(new)
        if n%2==0:
            return (new[n//2]+new[(n//2)-1])/2
        else:
            return new[n//2]
        
        
        
        
        ''' Brute Force '''
        
        new=sorted(nums1+nums2)
        n=len(new)
        if n%2==0:
            return (new[n//2]+new[(n//2)-1])/2
        else:
            return new[n//2]