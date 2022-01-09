class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left, right=0,9
        seen, res=set(), set()
        while right<len(s):
            cur=s[left:right+1]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
            left+=1
            right+=1
        return res