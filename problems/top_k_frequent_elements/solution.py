class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=Counter(nums)
        pq=[(-v,k) for k,v in cnt.items()]
        heapq.heapify(pq)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(pq))
        return [i[1] for i in res]