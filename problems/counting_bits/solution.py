class Solution:
    def countBits(self, num: int) -> List[int]:
        '''
        countBits(N) = countBits(2N)
        countBits(N)+1 = countBits(2N+1)
        '''
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter

        
        
        '''-------------'''
        res=[]
        for i in range(num+1):
            cnt=0
            while i:
                cnt+=1
                i=i&(i-1)
            res.append(cnt)
        return res