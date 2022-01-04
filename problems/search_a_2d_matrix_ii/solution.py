class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        '''Start from top right'''
        # row,col=0,len(matrix[0])-1
        # while col>=0 and row<len(matrix):
        #     if target<matrix[row][col]:
        #         col-=1
        #     elif target>matrix[row][col]:
        #         row+=1
        #     else:
        #         return True
        # return False
        
        '''Binary search in each row nlogn'''
        def binarySearch(arr):
            left, right=0,len(arr)
            while left<right:
                mid=left + (right - left)//2
                if target<arr[mid]:
                    right=mid
                elif target>arr[mid]:
                    left=mid+1
                else:
                    return True
            return False
        
        for row in range(len(matrix)):
            if target>matrix[row][-1]:
                continue
            if binarySearch(matrix[row]):
                return True
        return False
        
        
        '''Brute force'''
        m=len(matrix)
        n=len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==target:
                    return True
        return False