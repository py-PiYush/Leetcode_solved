class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt=0
        for i in J:
            cnt+=S.count(i)
        return cnt
            