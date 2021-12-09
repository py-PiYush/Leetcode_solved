from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.check=[0]*len(arr)
        # return self.dfsRec(arr,start)
        return self.bfs(arr,start)
        
    def dfsRec(self, arr,start):
        i=start
        if i<0 or i>=len(arr):
            return False
        if self.check[i]:
            return False
        self.check[i]=1
        if arr[i]==0:
            return True

        forward=self.dfsRec(arr,i+arr[i])
        back=self.dfsRec(arr,i-arr[i])
        return forward or back
            
    def bfs(self, arr, start):
        indexes=deque([start])
        while indexes:
            i=indexes.popleft()
            if arr[i]==0:
                return True
            if self.check[i]:
                continue
            self.check[i]=1
            if i+arr[i]<len(arr):
                indexes.append(i+arr[i])
            if i-arr[i]>=0:
                indexes.append(i-arr[i])
        return False
        
