class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        for i in nums:
            i=math.floor(math.log10(i))+1
            print(i)
            if not i%2:
                even+=1
        return even
                
                
        