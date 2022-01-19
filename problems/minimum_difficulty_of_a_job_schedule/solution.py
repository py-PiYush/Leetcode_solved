class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        '''Bottom up'''
        n = len(jobDifficulty)
        # If we cannot schedule at least one job per day, 
        # it is impossible to create a schedule
        if n < d:
            return -1
        
        dp = [[float("inf")] * (d + 1) for _ in range(n)]
        
        # Set base cases
        dp[-1][d] = jobDifficulty[-1]

        # On the last day, we must schedule all remaining jobs, so dp[i][d]
        # is the maximum difficulty job remaining
        for i in range(n - 2, -1, -1):
            dp[i][d] = max(dp[i + 1][d], jobDifficulty[i])

        for day in range(d - 1, 0, -1):
            for i in range(day - 1, n - (d - day)):
                hardest = 0
                # Iterate through the options and choose the best
                for j in range(i, n - (d - day)):
                    hardest = max(hardest, jobDifficulty[j])
                    # Recurrence relation
                    dp[i][day] = min(dp[i][day], hardest + dp[j + 1][day + 1])

        return dp[0][1]
        
        
        
        '''top down'''
        @lru_cache(None)
        def dp(i, day):
            #base case
            if day==d:
                return hardest_job_remaining[i]
            
            #recurrence relation
            best=float('inf')
            hardest=0
            for j in range(i, n-(d-day)):
                hardest=max(hardest, jobDifficulty[j])
                best=min(best, hardest+ dp(j+1, day+1))
            
            return best
        
        #Main
        
        n=len(jobDifficulty)
        
        #not possible if no. of jobs < no. of days
        if n<d: return -1
        
        #Find hardest job remaining for all the days
        hardest=0
        hardest_job_remaining=[0]*n
        for i in range(n-1, -1,-1):
            hardest=max(hardest, jobDifficulty[i])
            hardest_job_remaining[i]=hardest
        
        return dp(0,1)
        