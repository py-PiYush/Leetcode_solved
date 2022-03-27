class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        '''Binary search + heap'''
        import heapq
        def count_ones(arr):
            lo,hi=0,len(arr)
            while lo<hi:
                mid=lo+ (hi-lo >> 1)
                if arr[mid]==1:
                    lo=mid+1
                else:
                    hi=mid
            return lo
        
        oneIdx=[[count_ones(row),i] for i,row in enumerate(mat)]
        return [ res[1] for res in heapq.nsmallest(k, oneIdx)]
        
        
        
        
        # res=[]
        # for i in range(len(mat)):
        #     res.append([i,sum(mat[i])])
        # final= sorted(res,key=lambda x:x[1])
        # return [i[0]for i in final][:k]
    
    
    
#         scores = list(map(lambda l: sum(l), mat))
#         scores_enum = list(enumerate(scores))
#         print(scores_enum)
        
#         ordered = sorted(scores_enum, key=lambda el: el[1])
        
#         return [ordered[i][0] for i in range(k)]

        