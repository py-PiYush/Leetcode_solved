
from itertools import combinations

class Solution:
    
        
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def good(m,n,o):
            if abs(m-n)>a:
                return False
            elif abs(n-o)>b:
                return False
            elif abs(m-o)>c:
                return False
            return True
        
        
        cnt=0
        for i in (list(combinations(arr,3))):
            if good(i[0],i[1],i[2]):
                cnt+=1
        return cnt
        