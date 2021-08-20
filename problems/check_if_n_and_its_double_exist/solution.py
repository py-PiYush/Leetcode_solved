class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        #O(n)
        s=set()
        for i in arr:
            if i*2 in s or i/2 in s:
                return True
            s.add(i)
        return False
            
        
        #O(n^2)
        # if arr.count(0)>1:
        #     return True
        # for i in arr:
        #     if 2*i in arr and i!=0:
        #         return True
        # return False