class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        new=map(str,nums)
        return len([len(i) for i in new if len(i)%2==0])
        