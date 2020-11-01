class Solution:
    def titleToNumber(self, s: str) -> int:
        ttonum=dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),range(1,27)))
        #print(ttonum)
        num=0
        times=0
        for i in s[::-1]:
            num+=(26**times)*ttonum[i]
            times+=1
        return num