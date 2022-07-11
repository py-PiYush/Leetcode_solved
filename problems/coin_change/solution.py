class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         def recur(W,n):
# 			#base condition
#             if W==0:
#                 return 0
#             if n==0:
#                 return float('inf')
#             if memo[n][W]!=-1:
#                 return memo[n][W]
#             #condition 1
#             if coins[n-1] <= W:
#                 choose = 1 + recur(W - coins[n-1], n)
#                 ignore = recur(W, n-1)
#                 memo[n][W] = min(choose, ignore)
#             #condition 2
#             else:
#                 memo[n][W] = recur(W, n-1)
#             return memo[n][W]
        
#         n = len(coins)
#         memo = [[-1 for i in range(amount + 1)] for j in range(n + 1)]
#         ans = recur(amount, n)
#         return ans if ans!=float('inf') else -1
        
        
        ''' bottom up'''
        dp=[0]+[float('inf')]*amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]=min(dp[i], 1 + dp[i-coin])
        print(dp)
        return dp[amount] if dp[amount]!=float('inf') else -1
    
        ''' 2D dp'''
        dp = [[0 for _ in range(amount+1)]for __ in range(len(coins)+1)]
        for j in range(1,amount+1):
            dp[0][j]=float('inf')
        # print(dp)
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1]<=j:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        ans = dp[len(coins)][amount]
        return ans if ans!=float('inf') else -1
        
        
        
        '''top down'''
        @lru_cache(None)
        def dp(i): #return fewest number of coins to make up 'i' money
            
            #base case
            if i==0:
                return 0
            
            fewest=float('inf')
            for coin in coins:
                if i-coin>=0:
                    fewest=min(fewest, 1 + dp(i-coin))
            return fewest
        
        ans = dp(amount)
        return ans if ans!=float('inf') else -1
            