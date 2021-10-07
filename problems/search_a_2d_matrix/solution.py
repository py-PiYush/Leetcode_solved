class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up,down=0,len(matrix)-1
        row=-1
        while up<=down:
            mid=(up+down)//2
            if matrix[mid][0]>target:
                down=mid-1
            elif matrix[mid][-1]<target:
                up=mid+1
            else:
                row=matrix[mid]
                break
                
        print(row)
        if row==-1:
            return False
        
        left,right=0,len(row)-1
        while left<=right:
            mid=(left+right)//2
            if row[mid]==target:
                return True
            elif row[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False