class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        preXOR=[arr[0]]*len(arr)
        d={0:[-1]}
        count,cur=0,0
        for i in range(len(arr)):
            cur^=arr[i]
            if cur in d:
                tmp=[i-x-1 for x in d[cur]]
                count+=sum(tmp)
                d[cur].append(i)
            else:
                d[cur]=[i]
        return count
                
        
                