class Solution:
    def minDeletions(self, s: str) -> int:
        
        
        freq = Counter(s)
        heap = [-v for v in freq.values() if v!=0]
        heapq.heapify(heap)
        ans = 0
        while len(heap)>1:
            val = -heapq.heappop(heap)
            if val == -heap[0]:
                if val-1>0:
                    val-=1
                    heapq.heappush(heap, -val)
                ans+=1
        return ans
        
        
        
        
        '''----------------------'''
        freq = Counter(s)
        # print(freq)
        seen=set()
        ans=0
        for k in freq:
            while freq[k] in seen and freq[k]!=0:
                freq[k]-=1
                ans+=1
            seen.add(freq[k])
        return ans
                
        