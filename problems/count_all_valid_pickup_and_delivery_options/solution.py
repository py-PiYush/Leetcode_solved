class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def totalWays(unpicked, undelivered):
            if unpicked == undelivered == 0:
                return 1
            if unpicked<0 or undelivered<0 or undelivered<unpicked:
                return 0
            
            ans = unpicked*totalWays(unpicked-1, undelivered)
            ans%=MOD
            
            ans+= (undelivered - unpicked)*totalWays(unpicked, undelivered -1)
            ans%=MOD
            
            return ans
        
        return totalWays(n, n)
        