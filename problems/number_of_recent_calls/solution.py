class RecentCounter:

    def __init__(self):
        self.cnt=collections .deque()
        

    def ping(self, t: int) -> int:
        
        self.cnt.append(t)
        last=t-3000
        while self.cnt[0]<last:
            self.cnt.popleft()
       
        return len(self.cnt)
        
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
        '''#TLE
        self.cnt.append(t)
        last=self.cnt[-1]-3000
        req=len(self.cnt)

        for i in self.cnt:
            if i<last:
                req-=1
            elif i>=last:
                break'''