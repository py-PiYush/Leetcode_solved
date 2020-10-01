class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig=map(str,digits)
        return list(str(int(''.join(dig))+1))