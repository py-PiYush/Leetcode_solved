class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        @lru_cache(None)
        def recurse(idx):
            res = clubbed[idx][1]
            for i in range(idx+1, len(ages)):
                if clubbed[idx][1]>=clubbed[i][1]:
                    res = max(res, recurse(i) + clubbed[idx][1])
            return res
        
        
        clubbed = sorted(zip(ages, scores), key = lambda x: (-x[0], -x[1]))
        # print(clubbed)
        ans = 0
        for i in range(len(ages)):
            ans=max(ans, recurse(i))
        return ans
    
        ''''''
        @lru_cache(None)
        def recur(idx, maxAgeSoFar):
            # nonlocal score
            if idx==len(scores):
                return 0
            if clubbed[idx][1]>=maxAgeSoFar:
                score=max(clubbed[idx][0]+recur(idx+1, clubbed[idx][1]), recur(idx+1, maxAgeSoFar))
            else:
                score=recur(idx+1, maxAgeSoFar)
            return score
        
        clubbed = sorted(zip(scores, ages))
        score = 0
        return recur(0,0)
        
        
        ''' MLE '''
        @lru_cache(None)
        def recur(idx, minSoFar):
            nonlocal score
            if idx==len(ages):
                return 0
            if clubbed[idx][1]<=minSoFar:
                score=max(clubbed[idx][1]+recur(idx+1, clubbed[idx][1]), recur(idx+1, minSoFar))
            else:
                score=recur(idx+1, minSoFar)
            return score
        
        clubbed = sorted(zip(ages, scores), key = lambda x: (-x[0], -x[1]))
        score = 0
        return recur(0,float('inf'))