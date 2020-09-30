class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #if len(arr)==1:
         #   return arr
        
        
        max=arr[-1]
        i=len(arr)-2
        while i>=0:
            tmp=arr[i]
            arr[i]=max
            if tmp>max:
                max=tmp
            
            i-=1
        
        arr[-1]=-1
        return arr
        
        