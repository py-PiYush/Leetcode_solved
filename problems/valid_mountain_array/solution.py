class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length=len(A)
        
        if length<3:
            return False
        
        first=[A[0]]+[A[i] for i in range(1,length) if A[i]>A[i-1]]
        last=[A[i+1] for i in range(0,length-1) if A[i]>A[i+1]]
        
        if len(last)==0 or len(first)==1:
            return False
        
        if first+last!=A:
            return False
    
        
        
        
        
        return True
        