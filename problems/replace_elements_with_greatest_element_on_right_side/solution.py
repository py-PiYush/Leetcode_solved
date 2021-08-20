class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if arr==[]:
            return arr
        
        max_=arr[-1]
        arr[-1]=-1
        i=len(arr)-2
        while i>=0:
            temp=arr[i]
            arr[i]=max_
            max_=max(temp, max_)
            i-=1
        return arr