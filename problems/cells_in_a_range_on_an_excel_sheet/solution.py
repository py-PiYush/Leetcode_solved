class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        lo, hi = s.split(':')
        r1, c1 = int(lo[1]), ord(lo[0])
        r2, c2 = int(hi[1]), ord(hi[0])
        return [chr(c)+str(r) for c in range(c1, c2+1) for r in range(r1, r2+1)]