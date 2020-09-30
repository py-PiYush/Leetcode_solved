class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i=0
        j=0
        for i in range(len(A)):
            if A[i]%2==0:
                A[j],A[i]=A[i],A[j]
                j+=1
        return A  
        