class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # return sorted([i**2 for i in A])
        
        pos=self.first_non_negative(A)
        neg=pos-1
        res=[]
        
        print(pos,neg)
        
        while pos<len(A) and neg>=0:
            if A[pos]**2 <= A[neg]**2:
                res.append(A[pos]**2)
                pos+=1
            else:
                res.append(A[neg]**2)
                neg-=1
                
        if pos>=len(A) and neg>=0:
            res+=[i**2 for i in A[neg::-1]]
        if neg<0 and pos<len(A):
            res+=[i**2 for i in A[pos:]]
        return res
    
    def first_non_negative(self,A):
        for i in range(len(A)):
            if A[i]>=0:
                return i
        return len(A)
                