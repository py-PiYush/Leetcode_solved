class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        cnt=0
        for c in c1:
            if c in c2:
                cnt+= abs(c1[c] - c2[c])
            else:
                cnt+= c1[c]
        for c in c2:
            if c not in c1:
                cnt+=c2[c]
        return cnt