class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=len(nums)
        evenCount, oddCount = defaultdict(int), defaultdict(int)
        for i in range(0,n, 2):
            evenCount[nums[i]]+=1
            if i<n-1:
                oddCount[nums[i+1]]+=1
        max_even, second_max_even = (None, 0), (None, 0)
        for num, cnt in evenCount.items():
            if cnt>max_even[1]:
                max_even, second_max_even = (num, cnt), max_even
            elif cnt>second_max_even[1]:
                second_max_even = (num, cnt)
        
        max_odd, second_max_odd = (None, 0), (None, 0)
        for num, cnt in oddCount.items():
            if cnt>max_odd[1]:
                max_odd, second_max_odd = (num, cnt), max_odd
            elif cnt>second_max_odd[1]:
                second_max_odd=(num, cnt)
        
        if max_even[0] == max_odd[0]:
            return min(n-max_even[1]-second_max_odd[1], n-second_max_even[1]-max_odd[1])
        return n-max_even[1]-max_odd[1]