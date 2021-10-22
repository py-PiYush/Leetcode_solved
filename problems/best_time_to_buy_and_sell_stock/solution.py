class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit=0
        # min_,max_=0,0
        # while max_<len(prices):
        #     if prices[min_]>prices[max_]:
        #         min_=max_
        #     profit=prices[max_]-prices[min_]
        #     maxProfit=max(maxProfit, profit)
        #     max_+=1
        # return maxProfit
        maxCur,maxSoFar=0,0
        for i in range(1,len(prices)):
            maxCur+=prices[i]-prices[i-1]
            maxCur=max(0,maxCur)
            maxSoFar=max(maxCur,maxSoFar)
        return maxSoFar
            