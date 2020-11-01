class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=dict(zip(list('balon'),[0,0,0,0,0]))
        #print(count)
        for i in text:
            if i in 'ban':
                count[i]+=1
            elif i in 'lo':
                count[i]+=0.5

        return(int(min(count.values())))
        