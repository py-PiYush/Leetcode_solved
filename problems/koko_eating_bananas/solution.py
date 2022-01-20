class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):
            rem=h
            for pile in piles:
                rem-=math.ceil(pile/k)
                if rem<0:
                    return False
            return True

        left, right=math.ceil(sum(piles)/h), max(piles)
        while left < right:
            mid=left+(right-left)//2
            if feasible(mid):
                right=mid
            else:
                left=mid+1
        
        return left