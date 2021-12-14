class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        '''Heap'''
        # import heapq
        # pq=[-i for i in stones]
        # heapq.heapify(pq)
        # print(pq)
        # while len(pq)>1:
        #     a=-(heapq.heappop(pq))
        #     b=-(heapq.heappop(pq))
        #     if b<a:
        #         heapq.heappush(pq, b-a)
        # return -heapq.heappop(pq) if pq else 0
    
        '''Sorting'''
        stones.sort()
        while len(stones)>1:
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-2]=stones[-1]-stones[-2]
                stones.pop()
                stones.sort()
        return stones[0] if stones else 0