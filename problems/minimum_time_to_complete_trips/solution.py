class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        arr=[1/n for n in time]
        left = math.ceil(totalTrips/sum(arr))
        right = totalTrips*min(time)
        while left<right:
            mid=left + (right - left)//2
            if sum([mid//n for n in time])>=totalTrips:
                right=mid
            else:
                left=mid+1
        return left