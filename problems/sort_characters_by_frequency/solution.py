class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter

        
        '''Using Counter + heap'''
        import heapq
        cnt=Counter(s)
        
        heap=[(-v,k) for k, v in cnt.items()]
        heapq.heapify(heap)
        
        res=[]
        while heap:
            v,k=heapq.heappop(heap)
            res+=[k]*(-v)
        return ''.join(res)
        
        
        
        '''Using Counter'''
        # count=Counter(s)
        # lst=sorted(count, key=lambda x: (-count[x], x))
        # print(count, lst)
        # res=''
        # for i in lst:
        #     res+=i*count[i]
        # return res
    
        '''Using Counter + bucket sort'''
#         cnt = Counter(s)
#         n = len(s)
#         bucket = [[] for _ in range(n+1)]
#         for c, freq in cnt.items():
#             bucket[freq].append(c)
        
#         ans = []
#         for freq in range(n, -1, -1):
#             for c in bucket[freq]:
#                 ans.append(c * freq)
#         return "".join(ans)