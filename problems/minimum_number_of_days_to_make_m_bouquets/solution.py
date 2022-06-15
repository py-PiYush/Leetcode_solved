class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def condition(days):
            flowers, boq = 0, 0
            for d in bloomDay:
                flowers=(flowers+1, 0)[d>days]
                if flowers>=k:
                    flowers = 0
                    boq+=1
                    if boq==m:
                        return True
            return False
            
        if m*k>len(bloomDay): return -1
        
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left