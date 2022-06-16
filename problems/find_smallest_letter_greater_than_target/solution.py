class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def condition(char):
            return char>target
            
            
        left, right = 0, len(letters)-1
        while left<right:
            mid = left + (right - left)//2
            if condition(letters[mid]):
                right = mid
            else:
                left = mid+1
        return letters[left] if letters[left]>target else letters[0]