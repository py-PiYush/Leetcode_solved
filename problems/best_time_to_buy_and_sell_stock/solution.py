class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''O(n^2)'''
        # profit=0
        # for i in range(len(prices)-1):
        #     profit=max(profit,max([prices[j]-prices[i] for j in range(i+1,len(prices))]))
        # return profit
        
        minprice,maxprofit=sys.maxsize,0
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            elif prices[i]-minprice>maxprofit:
                maxprofit=prices[i]-minprice
        return maxprofit
            