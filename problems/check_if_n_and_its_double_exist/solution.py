class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set(arr)
        return arr.count(0) > 1 or any(2 * x in s for x in s if x)
        