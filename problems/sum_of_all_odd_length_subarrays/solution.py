#from itertools import combinations
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_=0
        i=0
        j=0
        while i<len(arr):
            j=i
            while j<len(arr):
                sum_+=(sum(arr[i:j+1]))
                j+=2
            i+=1
        return sum_
        
            
        