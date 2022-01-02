class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        '''Brute Force'''
        # cnt=0
        # for i in range(len(time)):
        #     for j in range(i+1, len(time)):
        #         if (time[i]+time[j])%60==0:
        #             cnt+=1
        # return cnt
    
        '''two sum problem (target=60)'''
        lst=[i%60 for i in time]
        cnt=0
        c=[0]*61
        for n in lst:
            cnt+=c[60-n]
            c[n if n else 60]+=1
            
        
        return cnt