class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        print(count)
        longest=0
        odd=False
        for value in count.values():
            if value%2==0:
                longest+=value
            else:
                odd=True
                longest+=value-1
        return longest+1 if odd else longest