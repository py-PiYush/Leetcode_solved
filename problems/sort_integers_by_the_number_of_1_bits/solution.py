class Solution:
    def count1(self,n):
        b=bin(n).count('1')
        return b
        
        
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        return(sorted(arr,key=(self.count1)))