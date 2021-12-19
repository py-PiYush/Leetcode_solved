class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.pq=[i for i in self.nums[:self.k]]
        heapq.heapify(self.pq)
        for x in self.nums[self.k:]:
            heapq.heappushpop(self.pq, x)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq)>self.k:
            heapq.heappop(self.pq)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)