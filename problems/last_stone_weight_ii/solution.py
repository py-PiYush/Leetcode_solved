class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
#         total = sum(stones)
        
#         Max_weight = int(total/2)
        
#         current = (Max_weight+1)*[0]
        
#         for v in stones:
#             for w in range(Max_weight, -1, -1):
#                 if w-v>=0:
#                     current[w] = max(v + current[w-v], current[w])
        
#         return total-2*current[-1]
        
    
        '''------- Minimum Subset sum difference ----------'''
        total, n = sum(stones), len(stones)
        half_sum = total//2
        print(total, half_sum)
        
        dp=[[False]*(half_sum+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
            
        for i in range(1, n+1):
            for j in range(1, half_sum+1):
                if stones[i-1]<=j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-stones[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        sum1 = half_sum - dp[-1][::-1].index(True)
        return total - 2*sum1