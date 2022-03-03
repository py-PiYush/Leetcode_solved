#from itertools import combinations
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_=0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                sum_+=sum(arr[i:j+1])
        return sum_
            
        