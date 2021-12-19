class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lastFruit, secondLastFruit =-1,-1
        lfCount=0
        cur=0
        maxLen=0
        for f in fruits:
            if f in (lastFruit, secondLastFruit):
                cur+=1
                if f==lastFruit:
                    lfCount+=1
                else:
                    lfCount=1
                    secondLastFruit=lastFruit
                    lastFruit=f
            else:
                cur=lfCount+1
                lfCount=1
                secondLastFruit=lastFruit
                lastFruit=f
            maxLen=max(maxLen, cur)
        return maxLen