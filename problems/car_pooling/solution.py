class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        maxEnd=max(i[2] for i in trips)
        diff=[0]*(maxEnd+1)
        for count, start, end in trips:
            diff[start]+=count
            diff[end]-=count
            
        tot=0
        for i in diff:
            tot+=i
            if tot>capacity:
                return False
        return True
        
        
        lst=[]
        for n,start, end in trips:
            lst+=[(start, n), (end, -n)]
            
        lst.sort()
        cap=0
        for i in lst:
            cap+=i[1]
            if cap>capacity:
                return False
        return True